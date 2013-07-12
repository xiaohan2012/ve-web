from pymongo import MongoClient

username = "xiaohan"
password = "xh24206688"

conn = MongoClient("mongodb://%s:%s@dharma.mongohq.com:10071/ve-web" %(username, password))
print conn