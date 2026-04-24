import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")


uri = f"mongodb://{user}:{password}@{host}:27017/"
client = MongoClient(uri)

@app.route('/')
def hello():
    try:
        client.admin.command('ping')
        return "Connected to MongoDB successfully!"
    except Exception as e:
        return f"Connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)