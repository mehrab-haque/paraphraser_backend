from logic import makeEasy
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/paraphrase',methods=['POST'])
def hello_world():
    content=request.json
    return jsonify({"text": makeEasy(content["text"])})

app.run()