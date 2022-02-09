Site created by [DEVMAN](https://dvmn.org)  
```active_passcards_view```, ```passcard_info_view```, ```storage_information_view``` by [@IlyaShirko](https://github.com/ilyashirko/)

# SECURITY CONTROL PANEL
Site was made for the security officers to control security access cards of company employees which visit secret storage.  

## How to run
For local running you should install requirements.txt via pip or pip3:  
```
pip3 install -r requirements.txt
```  

Then check `settings.py` for correct database settings and start local server from root directory via:  
```
python3 main.py runserver
```

You can see site on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

# Main scripts description
## active_passcards_view.py
display all active security cards on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  

## storage_information_view.py  
display all non-closed visits (employees in storage now) on [/storage_information](http://127.0.0.1:8000/storage_information)

## passcard_info_view.py  
display all visits of choosen employee with a note whether the visit was longer than an hour
