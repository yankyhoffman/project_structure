import logging
import logging.handlers
import os

_base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_log_dir = os.path.join(_base_dir, '.log')

def get_project_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    h_logfile = logging.handlers.TimedRotatingFileHandler(
        filename=os.path.join(_log_dir, f"{name}.log"), when='D', backupCount=10
    )
    h_logfile.setLevel(logging.INFO)
    h_logfile.setFormatter(
        logging.Formatter('[%(asctime)s - %(levelname)s] %(message)s <%(module)s|%(funcName)s|%(thread)d>')
    )

    logger.addHandler(h_logfile)
    return logger
