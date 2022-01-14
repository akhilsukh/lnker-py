# Guide to CLI commands for LNK
### Environment
- creating environment: `python3 -m venv env`
- activating environment: `source env/bin/activate`
- deactivating environment: `deactivate`

### Pip Packages
- installing from requirements file: `python3 -m pip install -r requirements.txt`
- backing up to requirements file: `python -m pip freeze > requirements.txt`

### Environment Variables 
- setting environment variable: `export DATABASE_URL="postgresql://localhost/lnk"`

### Jumpstarting Server
- starting postgresql server: `sudo service posgresql start`
- stopping postgresql server: `sudo service postgresql stop`
- restarting postgresql server: `sudo service postgresql restart`

### Finding databases and tables
- starting postgres session: `sudo -i -u postgres`
- starting psql session: `psql`
- connect to database: `\c lnk`
- list tables in database: `\dt` or `\z`
- print table: `TABLE links`
