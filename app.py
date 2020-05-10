from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
import os

app = Flask(__name__)
app.config.from_pyfile(os.path.join(".", "config/app.conf"), silent=False)
app.config["MONGO_URI"] = app.config.get("MONGODB_URL")
mg = PyMongo(app)


@app.route('/')
def customer():
    customers = mg.db.customers.find({"name": "John"}, {"_id": 0, "name": 1, "address": 1})
    return dumps(customers[0])


if __name__ == '__main__':
    app.run(debug=True)
