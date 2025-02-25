# Python Version and Package Management

## Prerequisites

### Linux
- pyenv 
- pyenv-virtualenvs

### Windows
- pyenv-win

### Install Version
- To install a version for pyenv run the following command:
`pyenv install [version]`
- Note the current project version is 3.13.2.

## Usage
- pyenv uses the `.python-version` file to manage the project version of python.
    * The virtual environment should start up automatically when you enter the project directory.
- pyenv uses `requirements.txt` to manage the project packages and their versions.
    * To update/install the packages run `pip install -r requirements.txt`
    * If a new package is installed update the `requirements.txt` file by running:
    `pip freeze > requirements.txt`
