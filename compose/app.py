from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB using the credentials from docker-compose
client = MongoClient(
    host="mongodb",
    port=27017,
    username=os.environ.get("MONGO_INITDB_ROOT_USERNAME", "admin"),
    password=os.environ.get("MONGO_INITDB_ROOT_PASSWORD", "supersecret")
)
db = client["mydb"]

@app.route("/")
def index():
    return jsonify({"status": "Flask is running!"})

@app.route("/health")
def health():
    # Quick MongoDB connectivity check
    try:
        client.admin.command("ping")
        return jsonify({"status": "ok", "mongo": "connected"})
    except Exception as e:
        return jsonify({"status": "error", "mongo": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)