# coding = utf-8

from flask import Flask
app = Flask(__name__)

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



#
# 0. hello world #
#
@app.route('/')
def hello_world():
    log.debug('hello world')
    return 'Hello Python Web!'

if __name__ == '__main__':
    log.debug('############## main #################')
    app.run(host='0.0.0.0', port=1027, debug=True)


