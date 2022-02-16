Site created by [DEVMAN](https://dvmn.org)  
```active_passcards_view```, ```passcard_info_view```, ```storage_information_view``` by [@IlyaShirko](https://github.com/ilyashirko/)

# SECURITY CONTROL PANEL
Site was made for the security officers to control security access cards of company employees which visit secret storage.  

## How to run
For local running you should clone repo, get in root directory, activate virtualenv and install requirements.txt via pip or pip3:  
```
$ git clone https://github.com/ilyashirko/django-orm-watching-storage
$ cd django-orm-watching-storage
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```  
create `.env` file and input there your database parameters and debug-mode status (true if you need debug, false if not)
```
DEFAULT_DATABASE_ENGINE=####.####.#######.########
DEFAULT_DATABASE_HOST=your.data.base
DEFAULT_DATABASE_PORT=2342
DEFAULT_DATABASE_NAME=name
DEFAULT_DATABASE_USER=user
DEFAULT_DATABASE_PASSWORD=password
DEBUG=TRUE
```

Then you can start local server from root directory via:  
```
python3 manage.py runserver
```

You can see site on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
