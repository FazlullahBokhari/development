from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Puppy </h1>"

@app.route('/info')
def info():
    return "<h1> Puppies are cuete </h1>"

@app.route('/<name>')
def puppy(name):
    return "<h1> This is a page for {} </h1>".format(name)

if __name__ == '__main__':
    app.run(debug=True)
