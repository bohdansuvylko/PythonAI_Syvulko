import logging

# logging.basicConfig(level=logging.INFO)
#
# logging.debug('debug description')
# logging.info('info description')
# logging.warning('info description')
# logging.error('error description')
# logging.critical('critical description')

logging.basicConfig(level=logging.DEBUG, filename='logs.log', filemode='w')
formate = "We have next logging message:%(asctime)s:%(levelname)s - %(message)s"

try:
    print(10/0)
except Exception:
    logging.exception("Exception")