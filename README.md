Installing System Packages

sudo apt update && sudo apt install -y make python3.12-venv tree wget

Cloning the Repository and Running Initialization

After setting up SSH and Git credentials, clone the repo

git clone <your-repo-url>
cd <your-repo-name>

Run the initialization script to set up

cd scripts/
chmod +x init.sh
./init.sh

This script ensures that Python, Make, and other dependencies are installed.

Setting Up a Virtual Environment

To maintain an isolated environment for dependencies:

cd scripts/
python3 -m venv env
source env/bin/activate

Installing Dependencies

Install the required Python libraries:

pip install -r requirements.txt

Required packages include:

pandas
lxml

Since the project relies on Chrome for rendering pages, install it manually:

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb

Verify installation:

google-chrome --version



**Scraping Yahoo Finance**

make -C scripts ygainers.html
make -C scripts ygainers.csv

**Scraping WSJ**

Since WSJ loads data dynamically, we configure Chrome to wait longer for JavaScript to render:

make -C scripts wjsgainers.html
make -C scripts wjsgainers.csv

Ensure the extracted files exist:

ls -l sample_data/

Organizing the Project Structure

Run:

tree -I env

Expected directory layout:

.
├── sample_data/
│   ├── ygainers.csv
│   ├── wjsgainers.csv
├── scripts/
│   ├── init.sh
│   ├── Makefile
│   ├── requirements.txt
├── README.md

Workflow for Updates and Version Control

Commit and push changes after modifying scripts or data:

git add .
git commit -m "Updated scripts and documentation"
git push origin main

Troubleshooting & Fixes

pandas.read_html() returns No tables found

Ensure WSJ pages are fully loaded by increasing Chrome's timeout (--virtual-time-budget=10000).

google-chrome-stable** not found**

Reinstall using wget and apt install.

Missing Python modules (ModuleNotFoundError****************************************************************************************************************************)

Ensure the virtual environment is active and install dependencies: pip install -r requirements.txt.
