#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:content>")
def print_string(content):
    print(content)
    return content


@app.route("/count/<int:num>")
def count(num):
    numbers = '\n'.join(str(i) for i in range(0, num + 1))
    print(numbers)
    return numbers


@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    result = None
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    elif operation == "%":
        result = num1 % num2

    if result is not None:
        return str(result)
    else:
        return "Invalid operation or parameters"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
