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

root.info("Hello, world")

try:

	exit(main())

except Exception:
	logging.exception('Exception in main()')
	exit(1)
