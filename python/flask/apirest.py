#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Working!"

@app.route('/api/<int:id>',methods=['GET'])
def getId(id):
    return str(id)

@app.route('/api',methods=['POST'])
def postId():
    return ""


if __name__ == '__main__':
    app.run(debug=True)