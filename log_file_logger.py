import logging
import logging.handlers
import os

handler = logging.handlers.WatchedFileHandler(
	os.environ.get('LOGFILE', 'python_logger.log'))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get('LOGLEVEL', 'INFO'))
root.addHandler(handler)

error_handler = logging.getLogger()
error_handler.setLevel(os.environ.get('LOGLEVEL', 'DEBUG'))
error_handler.addHandler(handler)

root.info("Hello, world")

error_handler.debug('Protocol problem: This big problem, really big')

try:

	exit(main())

except Exception:
	logging.exception('Exception in main()')
	exit(1)
