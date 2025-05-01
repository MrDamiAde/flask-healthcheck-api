from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/characters")
def get_characters():
    data = [
        {"name": "Loki", "health": 250},
        {"name": "Wolverine", "health": 350},
        {"name": "Scarlet Witch", "health": 250}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
