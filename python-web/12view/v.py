# coding = utf-8

from flask import Flask, request, render_template
from flask.views import View

app = Flask(__name__)
#app = Flask(__name__, template_folder='../templates')


if __name__ == '__main__':
    app.run(host='localhost', port=1027)
