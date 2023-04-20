#!/usr/bin/python3
# Setup a simple webserver with flask

from flask import Flask, redirect, request

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.before_request
def clear_trailing():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])


@app.route('/')
def helloBNB():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
