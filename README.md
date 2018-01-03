# appium_chatbot
### Installation
Firstly, you will need to [import db](#restore), and navigate to http://localhost:8001 after running the app.

* Use pip to install all required python packages
```sh
pip install -r requirements.txt
```
* Run setup script for setting up some default intents
```sh
$ python setup.py
```

* Development
```sh
$ python run.py
```

### DB
#### Backup
```
cd data/
mongodump --db=appiumbot
exit
```

#### Restore
```
cd data
mongorestore --drop --db=appiumbot --dir=dump/appiumbot/
exit
```
