# coding = utf-8

from flask import Flask, url_for
app = Flask(__name__)

# 10. response #


# 9. redirect #
# redirect(location)
# redirect(location, code=301)

# simple test
from flask import request, abort, redirect, url_for
app.config.from_object('config')

@app.route('/people/')
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return 'Name: {0}; UA: {1}'.format(name, user_agent)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return 'User: {} login'.format(user_id)
    else:
        return 'Open login page'

@app.route('/secret/')
def secret():
    abort(401)
    print 'This is never executed'


# 1. config #
#app.config['DEBUG'] = False

#app.config.update(
#        DEBUG=True,
#        SECRET_KEY='...'
#    )

app.config.from_object('settings')
import settings
app.config.from_object(settings)

app.config.from_pyfile('settings.py', silent=True)

# 2. logging #
import logging
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M:%S',
	filename='myapp.log',
	filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-8s %(levelname)-8s %(message)s')
console.setFormatter(formatter)

logging.getLogger('').addHandler(console)
log = logging.getLogger('xy')

# 3. debug #
#app.debug = True
#app.run()
#app.run(debug=True)


# 4. dynamic route #
@app.route('/item/<id>/')
def item(id):
    return 'Item:{}'.format(id)

@app.route('/<any(a, b):page_name>/')
def any():
    return 'any'

# 5. base converter #
import urllib
from werkzeug.routing import BaseConverter

class ListConverter(BaseConverter):
    def __init__(self, url_map, separator='+'):
        super(ListConverter, self).__init__(url_map)
        self.separator = urllib.unquote(separator)

    def to_python(self, value):
        return value.split(self.separator)

    def to_url(self, values):
        return self.separator.join(BaseConverter.to_url(value) 
                for value in values)

app.url_map.converters['list'] = ListConverter
@app.route('/list1/<list:page_names>/')
def list1(page_names):
    return 'Sepatator: {} {}'.format('+', page_names)

@app.route('/list2/<list(separator=u"|"):page_names>/')
def list2(page_names):
    return 'Sepatator: {} {}'.format('|', page_names)


# 6. http #
@app.route('/login', methods=['GET', 'POST'])
@app.route('/j/item/<id>', methods=['DELETE', 'POST'])

# 7. url #
@app.route('/projects/')
def projects():
    return 'The project page!'

@app.route('/about')
def about():
    return 'The about page!'

# 8. url for #
@app.route('/url/1')
def url(id):
    pass

with app.test_request_context():
    print url_for('url', id='1')
    print url_for('url', id=2, next='/')

#
# 0. hello world #
#
@app.route('/')
def hello_world():
    log.debug('hello world')
    return 'Hello Python Web!'

if __name__ == '__main__':
    log.debug('############## main #################')
    app.run(host='localhost', port=1027, debug=app.debug)
    #app.run(host='localhost', port=1027, debug=True)


