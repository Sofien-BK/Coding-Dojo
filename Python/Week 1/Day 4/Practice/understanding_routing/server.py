from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World!"
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/say/<string:name>')
def hi(name):
    return ("Hi " + name)
@app.route('/repeat/<int:num>/<string:name>')
def repeating(num , name):
    return (num * (' '+ name))











if __name__=="__main__":

    app.run(debug=True)