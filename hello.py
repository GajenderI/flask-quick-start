from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/api')
def hello():
   return "Hello World AsdfsdfPI"

def world():
   return "hello world"
app.add_url_rule("/a", "hello", world)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000,debug=True)