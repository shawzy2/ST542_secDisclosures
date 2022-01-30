# ST542 SEC Disclosures Investigation
Web scraping SEC 10-K reports to analyze the impact of diviserty declarations on company performance. This repo is responsible for scraping filings of select companies and identifying attributes of diversity reports. Analysis of significance of attributes will be done elsewhere.


# Setup Guide (MacOS)
* Clone repo in terminal `git clone https...`
* Install pip `python3 -m pip install --user --upgrade pip`
* Verify installation `python3 -m pip --version`
* Install virtual environment (allows us to download python packages) `python3 -m pip install --user virtualenv`
* Create virtual environment on machine `python3 -m venv env`
* Start virtualenv `source env/bin/activate`
* Install all packages from requirements.txt `pip install -r requirements.txt`
* Start jupyter notebook `jupyter notebook`
* Navigate to the notebook `notebook/scraper.ipynb`
