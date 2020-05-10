import pymongo
from flask import Flask
from bson.json_util import dumps


app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://ajith:*****@cluster0-b0lyy.mongodb.net/demo")
db = client.demo

@app.route('/')
def customer():
    customers = db.customers.find({"name": "John"}, {"_id": 0, "name": 1, "address": 1})
    return dumps(customers[0])


if __name__ == '__main__':
    app.run(debug=True)
