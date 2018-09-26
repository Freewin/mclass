import logging

logging.basicConfig(format='%(asctime)s     %(levelname)s:%(message)s',
                    datefmt='%m%d%Y %I:%M:%S %p',
                    level=logging.INFO,
                    filename='example.log'
                    )

logging.debug('This message will not print')
logging.info('This message will print')
logging.warning('This message will also print')

