from flask import Flask
import json

app = Flask(__name__)

@app.route('/hello')
def hello():
   return json.dumps({ 'hello': 'world' })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
