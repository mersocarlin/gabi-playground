#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

# Dummy Route for testing
@app.route('/_ping', methods=['GET'])
def get_test():
    return "Tested OK"

# Entry Point
if __name__ == '__main__':
    app.run(debug=True)
