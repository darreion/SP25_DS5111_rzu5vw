## Installing System Packages

Run the following command to update and install necessary packages:

```bash
sudo apt update && sudo apt install -y make python3.12-venv tree wget
```

## Cloning the Repository and Running Initialization

After setting up SSH and Git credentials, clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

Run the initialization script to set up dependencies:

```bash
cd scripts/
chmod +x init.sh
./init.sh
```

This script ensures that Python, Make, and other required tools are installed.

## Setting Up a Virtual Environment

To maintain an isolated environment for dependencies:

```bash
cd scripts/
python3 -m venv env
source env/bin/activate
```

## Installing Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

Required packages include:

```
pandas
lxml
```

## Installing Chrome for Headless Browsing

Since the project relies on Chrome for rendering pages, install it manually:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
```

Verify installation:

```bash
google-chrome --version
```

## Scraping Yahoo Finance Data

```bash
make -C scripts ygainers.html
make -C scripts ygainers.csv
```

## Scraping Wall Street Journal Data

Since WSJ loads data dynamically, we configure Chrome to wait longer for JavaScript to render:

```bash
make -C scripts wjsgainers.html
make -C scripts wjsgainers.csv
```

Ensure the extracted files exist:

```bash
ls -l sample_data/
```

## Project Directory Structure

To view the directory structure, run:

```bash
tree -I env
```

Expected layout:

```
.
├── sample_data/
│   ├── ygainers.csv
│   ├── wjsgainers.csv
├── scripts/
│   ├── init.sh
│   ├── Makefile
│   ├── requirements.txt
├── README.md
```

## Workflow for Updates and Version Control

Commit and push changes after modifying scripts or data:

```bash
git add .
git commit -m "Updated scripts and documentation"
git push origin main
```

## Troubleshooting & Fixes

- **`pandas.read_html()` returns `No tables found`**
  - Ensure WSJ pages are fully loaded by increasing Chrome's timeout (`--virtual-time-budget=10000`) {VERY IMPORTANT! Otherwise, the JS doesn't load the tables on the page so nothing gets parsed}.
- **`google-chrome-stable` not found**
  - Reinstall using `wget` and `apt install`.
- **Missing Python modules (`ModuleNotFoundError`)**
  - Ensure the virtual environment is active and install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

