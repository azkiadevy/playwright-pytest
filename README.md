# playwright-pytest framework codebase
Codebase for playwright using Pytest from Pyton

## Dependencies
1. Install Python 3.12, and 
2. (optional) Create the [environment for dependencies](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
3. Install Pytest `pip install pytest`
4. Install Pytest Playwright `pip install pytest-playwright`
5. Run `playwright install` to install the browser and 

## How to run the test
to running the test, 
1. go to tests file directory
2. run `pytest -s -v test_login.py --headed` "--headed" to make it headed the default browser is headless
