from loguru import logger
import sys 

def initalize_logger():
	fmt = "<green>[{time:YYYY-MM-DD HH:mm:ss}]</green> <level>[{level}]</level> | <cyan>{function}</cyan> | <level>{message}</level>"
	logger.remove()
	logger.add(sys.stderr, enqueue=True, format=fmt)
	logger.add("logs/fan_control_logs.log", retention="10 days", enqueue=True, format=fmt)