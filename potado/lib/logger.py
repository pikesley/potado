import logging

LOGGER = logging.getLogger("pig")
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(logging.StreamHandler())
