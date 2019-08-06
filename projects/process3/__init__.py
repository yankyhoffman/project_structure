from utils.logger import get_project_logger

logger = get_project_logger(__name__)
logger.debug(f"Logger initiated for {__name__}")

from . import process3
