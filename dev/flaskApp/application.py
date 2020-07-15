from flask import Flask, render_template
application = Flask(__name__)


@application.route('/')
def hello():
    return render_template('index.html')

@application.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    application.run(debug=True)