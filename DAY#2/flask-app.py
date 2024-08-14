from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!!"

@app.route('/getDetails')
def getDetails():
    return "Ritthyk M - 7376221CS280"

if __name__=='__main__':
    app.run(debug=True)
  
