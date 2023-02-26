# Introduction to Python

Repository to learn, try & test different python technologies

## Writing Unit Tests

Click this link to [Getting Started With Testing in Python](https://realpython.com/python-testing/)

## Creating a Python Virtual Environment

Click this link to [Creating Python Virtual Environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### Installing/Upgrading pip

Install or upgrade pip to the latest version  
`python3 -m pip install --user --upgrade pip`

Check pip version installed  
`python3 -m pip --version`

### Installing venv (or) virtualenv

Use `venv` for Python 3 or `virtualenv` for Python 2. Install virtualenv/venv using pip
`python3 -m pip install --user virtualenv`

### Creating a virtual environment

To create a virtual environment, go to your project’s directory and run venv. If you are using Python 2, replace venv with virtualenv in the below commands
`python3 -m venv <virtual-environment-name>`

### Activating a virtual environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it  
`source env/bin/activate`

### Leaving the virtual environment

If you want to switch projects or otherwise leave your virtual environment, simply run  
`deactivate`
