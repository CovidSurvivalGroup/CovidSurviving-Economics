from flask import Flask, render_template
application = Flask(__name__)


@application.route('/')
def hello():
    return render_template('index.html')

@application.route('/california')
def california():
    return render_template('california.html')

@application.route('/florida')
def florida():
    return render_template('florida.html')

@application.route('/newyork')
def newyork():
    return render_template('newyork.html')

@application.route('/texas')
def texas():
    return render_template('texas.html')


if __name__ == '__main__':
    application.run(debug=True)