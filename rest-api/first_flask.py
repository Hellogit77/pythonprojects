#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route("/devops", methods=['GET'])
def index():
    return "Hello World!"

if __name__ == '__name__':
    app.run(debug=True, host="0.0.0.0")
