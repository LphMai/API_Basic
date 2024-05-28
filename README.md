# 初步了解 API

# install
```python
pip install Flask
```

# main
```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/route', methods=['POST'])
def ping():
    return jsonify({'response': 'pong'})

if __name__ =='__main__':
    app.run(debug=True, port=8081)
```

# different route
```python
@app.route('/bang', methods=['GET'])
def bang():
    return jsonify({'response': 'bang'})
```

# return to web
(直接 return 語法)
```python
@app.route('/page_1', methods=['GET'])
def hello():
    return '<html><body><h1>Hello</h1></body></html>'
```
( 渲染頁面 )
```python
@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')
```