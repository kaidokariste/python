# Quick commands
```python --version``` - Pythoni versiooni kontrollimine  
```pip install --upgrade pymysql==0.8.0``` - paketi upgrade kui downgrade mingiks kindlaks versiooniks  
```pip install pymysql==0.8.0``` - kindle versiooni package installimine  
```venv\Scripts\activate.bat``` - Flask venv aktiveerimine  
```pip list``` - lists installed packages  
```pip show <package-name>``` - shows information of specific package

Get package version using __version__
```python
import pandas as pd

print(pd.__version__)
# 0.22.0
```

# Packages based on purpose
|Package name| Documentation  | Purpose  |  
|---|---|---|
| requests  | https://requests.readthedocs.io/en/latest/user/quickstart/  | API calls and processin libary  |  
| pandas    | https://pandas.pydata.org/docs/reference/index.html#api     | Pandas data frames and data manipulation package  | 
| dotenv    | https://pypi.org/project/python-dotenv/#getting-started     | Package to retrieve environment variables from .env file  | 

## Implementing .env
Assuming we have added line `api-token = "abcdef_123456"` to .env file  

```python
from dotenv import load_dotenv
load_dotenv()
import os
token = os.environ.get("api-token")
```
