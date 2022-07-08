from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    user_logged_in = True
    company = "Dell"
    letter = list(company)
    mylist = [10,20,30,40,50,60,72,80,90,100]
    return render_template('basic.html',variable =company, letters = letter,a_list = mylist, login=user_logged_in)


if __name__ == '__main__':
    app.run(debug=True)
