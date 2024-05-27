from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def ping():
    return jsonify({'response': 'pong'})

@app.route('/bang', methods=['GET'])
def bang():
    return jsonify({'response': 'bang'})

@app.route('/page_1', methods=['GET'])
def hello():
    return '<html><body><h1>Hello</h1></body></html>'

if __name__ =='__main__':
    app.run(debug=True, port=8081)