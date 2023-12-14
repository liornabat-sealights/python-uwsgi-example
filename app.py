
from flask import Flask
APP = Flask(__name__)

def say_hello():
    return "hello"


def say_goodbye():
    return "Goodbye for now"

@APP.route('/')
def index():
    return 'What to say: {}'.format(say_hello())


@APP.route('/goodbye')
def goodbye():
    return say_goodbye()


@APP.route('/hello')
def hello():
    return say_hello()


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=9092)
