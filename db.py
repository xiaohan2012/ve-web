from motor import MotorClient
from pymongo import MongoClient
username = "xiaohan"
password = "xh24206688"

connection_string = "mongodb://%s:%s@dharma.mongohq.com:10071/ve-web" %(username, password)

db = MongoClient()["ve-web"]
