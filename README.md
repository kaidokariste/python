# Quick commands
```python --version``` - Pythoni versiooni kontrollimine  
```pip install --upgrade pymysql==0.8.0``` - paketi upgrade kui downgrade mingiks kindlaks versiooniks  
```pip install pymysql==0.8.0``` - kindle versiooni package installimine  
```venv\Scripts\activate.bat``` - venv aktiveerimine (CMD)  
```venv\Scripts\activate.ps1``` - Python venv in Powershell environment. 
```pip list``` - lists installed packages  
```pip show <package-name>``` - shows information of specific package  
```pip install -r requirements.txt``` - Installing packages from requirements file

# Creating virtual environment in Python
```bash
[dbuser@localhost python-sandbox]$ python3 -m venv <folder name: usually venv>
[dbuser@localhost python-sandbox]$ ls
venv
[dbuser@localhost python-sandbox]$source venv/bin/activate
(venv) [dbuser@localhost bin]$
```

```
when it is powershell environment, then use
.venv\Scripts\activate.ps1 
```

Get package version using __version__
```python
import pandas as pd

print(pd.__version__)
# 0.22.0
```

# Updating Python in Ubuntu
Install all necessary linux packagaes, as missing one may start cousing some weard errors
```
$ sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
  libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libpq-dev
```
(as root) lets check out the Python version `# python3 --version`, it may show something like Python 3.6.8

Download and install Python from source
```
wget https://www.python.org/ftp/python/3.11.6/Python-3.11.6.tgz
tar xvf Python-3.11.6.tgz
cd Python-3.11.6
./configure --enable-optimizations
sudo make altinstall
```
Main idea is to unlink old binaries and link new binaries. Check out the new binaries from `[root@ctl ~]# cd /usr/local/bin`. Should be there after install.  
Move now to `cd /usr/bin` and `ls -lah`. You should see that symlink python3 points to old version etc.  

```
# Setting up python3 
ln -s /usr/local/bin/python3.11 python3.11
ln -sf python3.11 python3 # -f forces the symplink change as it already pointed to previous version 
```
And change other tihings similar way
```
#Setting up pip3
ln -s /usr/local/bin/pip3.11 pip3.11
ln -s pip3.11 pip3

#Clean up previous version links
rm pip-3
rm pip3.6

# Setting up python3.11-config
ln -s /usr/local/bin/python3.11-config python3.11-config
ln -sf python3.11-config python3-config

#Pydoc3
[root@ctl bin]# ln -s /usr/local/bin/pydoc3.11 pydoc3.11
[root@ctl bin]# ln -sf pydoc3.11 pydoc3
```
Final state should look like this
```
lrwxrwxrwx.   1 root root       8 Jul 13 08:50 pydoc3 -> pydoc3.11
lrwxrwxrwx.   1 root root      23 Jul 13 08:50 pydoc3.11 -> /usr/local/bin/pydoc3.11
lrwxrwxrwx.   1 root root       9 Jul 13 08:17 python3 -> python3.11
lrwxrwxrwx.   1 root root      24 Jul 13 08:14 python3.11 -> /usr/local/bin/python3.11
lrwxrwxrwx.   1 root root      31 Jul 13 08:40 python3.11-config -> /usr/local/bin/python3.11-config
lrwxrwxrwx.   1 root root      16 Jul 13 08:44 python3-config -> python3.11-config
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
