from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    lower_letter = False
    upper_letter = False
    num_end = False
    name = request.args.get('username')
    lower_letter = any(x.islower() for x in name)
    upper_letter = any(x.isupper() for x in name)
    num_end = name[-1].isdigit()
    report = lower_letter and upper_letter and num_end


    return render_template('report.html',report=report,lower_letter=lower_letter,upper_letter=upper_letter,num_end=num_end)


if __name__ == '__main__':
    app.run(debug=True)
