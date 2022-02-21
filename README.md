![example workflow](https://github.com/Alex2218/test-task-EZ/actions/workflows/github-action.yaml/badge.svg)
![Python](https://img.shields.io/badge/Python-Yes-green)

# Automatic-account-creation
This script is designed for educational purposes.

## About
The script automatically creates a discord account and logs into it by receiving an authorization token from the “authorization” headers.
- script accepts email and username on the command line
- password is generated automatically
- no need to verify email
- returns token to the command line after login

## Installation
- Copy repository
- Create a virtual environment in Linux:
```bash
python3 -m venv env
```
- Activate env:
```bash
source env/bin/activate
```
- Install packages:
```bash
pip install -r requirements.txt
```
- Run file `script.py`