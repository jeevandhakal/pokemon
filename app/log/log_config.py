import logging
from sqlalchemy.engine import Engine
from sqlalchemy import event

def configure_logging():
    # Configure the root logger
    logging.basicConfig(level=logging.INFO)  # Set your desired logging level

    # Configure SQLAlchemy logging
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy").setLevel(logging.INFO)

    # Register a custom event listener for SQLAlchemy to log SQL queries
    @event.listens_for(Engine, "before_cursor_execute")
    def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        logging.debug("SQL Query: %s", statement)
        logging.debug("Parameters: %s", parameters)
