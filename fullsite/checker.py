from flask import Flask, request, jsonify
from acceptURL import acceptURL
from flask_cors import cross_origin

app = Flask(__name__)

@app.route("/sendlink", methods=['POST'])
@cross_origin()
def main():
    urlGrab = acceptURL(request.json['url'])
    return jsonify(urlGrab.parseURL())

if __name__ == "__main__":
    app.run()
