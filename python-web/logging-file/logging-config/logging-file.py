# this is a simple example
import logging
import logging.config

#logging.basicConfig(filename='demo.log', filemode='w', level=logging.DEBUG)
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('XY')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
logger.debug('############################')
logger.debug('')
