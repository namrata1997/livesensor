from sensor.exception import SensorException
import sys
from sensor.logger import logging

def test_exception():
    try:
        logging.info("Testing the exception module")
        a=1/0
    except Exception as e:
        raise SensorException(e, sys) from e


if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)