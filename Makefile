default:
	@cat Makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate && pip install -r scripts/requirements.txt

ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	python3 -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wjsgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --disable-software-rasterizer --disable-dev-shm-usage --timeout=10000 --virtual-time-budget=10000 'https://www.wsj.com/market-data/stocks/us/movers' > wjsgainers.html

wjsgainers.csv: wjsgainers.html
	python3 -c "import pandas as pd; raw = pd.read_html('wjsgainers.html', flavor='lxml'); raw[0].to_csv('wjsgainers.csv')"

lint:
	pylint bin/normalize_csv.py

test: lint
	pytest -vv tests/


gainers:
	python3 get_gainer.py $(SRC)
