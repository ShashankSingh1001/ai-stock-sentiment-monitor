import logging
import os
import sys
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_dir = os.path.join(os.getcwd(), "logs")

os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s: %(message)s",
    level=logging.INFO,
)

console_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("[%(asctime)s] %(lineno)d %(name)s %(levelname)s: %(message)s")
console_handler.setFormatter(formatter)

if not any(isinstance(handler, logging.StreamHandler) for handler in logging.getLogger().handlers):
    logging.getLogger().addHandler(console_handler)

logging.info("Logger setup complete. Logging has started.")