from flask import Flask

app = Flask(__name__)


# python decorators
@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"


@app.route('/bye')
def say_bye():
    return '<p>Bye!!</p>'


if __name__=='__main__':
    app.run()


# python decorator function
# import time
#
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(5)
#         # do something before function
#         function()
#         function()
#         # do sth after function
#
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print('hello')
#
#
# @delay_decorator
# def say_buy():
#     print('Bye')
#
#
# def say_greeting():
#     print('How are you???')
#
#
# decorator_function = delay_decorator(say_greeting)
# decorator_function()
