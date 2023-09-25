import logging

from db.init_db import init_db
from tests.utils.dependencies import db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_database():
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init_database()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
