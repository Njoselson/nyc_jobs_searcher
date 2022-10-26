import logging
import os

logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO"),
    datefmt="%Y-%m-%dT%H:%M",
    format="[%(asctime)s.%(msecs)03dZ]: %(levelname)s: [%(module)s - L%(lineno)d] %(message)s",
)

LOGGER = logging.getLogger("transcript-service")
