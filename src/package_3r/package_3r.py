"""Example module for the demo package"""

from .logger_config import logger


def hello_world(message):
    """Example function to say Hello world with a message"""
    logger.debug("This is DEBUG level log message")
    logger.info("This is INFO level log message")
    logger.warning("This is WARN level log message")
    logger.error("This is ERROR level log message")
    return f"Hello world!: {message}"

def calculate_mean(values):
    """Calculate the arithmetic mean of numerical values."""
    if not values:
        raise ValueError("The input must not be empty.")

    return sum(values) / len(values)