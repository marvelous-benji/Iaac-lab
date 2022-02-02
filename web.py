from flask import Flask, jsonify
from flask import Response


app: Flask = Flask(__name__)


@app.route("/")
def home() -> Response:
    return jsonify({"status":"success","msg":"Hello World"})


if __name__ == '__main__':
    app.run()