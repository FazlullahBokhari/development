from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    company = "Dell"
    letter = list(company)
    return render_template('basic.html',variable =company, letters = letter)


if __name__ == '__main__':
    app.run(debug=True)
