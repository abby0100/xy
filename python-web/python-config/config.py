
# coding = utf-8

from flask import Flask
app = Flask(__name__)

# config #
app.config['DEBUG'] = False

app.config.update(
        DEBUG=True,
        SECRET_KEY='...'
    )

app.config.from_object('settings')
import settings
app.config.from_object(settings)

app.config.from_pyfile('settings.py', silent=True)

@app.route('/')
def hello_world():
    return 'Hello Python Web!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1027)

