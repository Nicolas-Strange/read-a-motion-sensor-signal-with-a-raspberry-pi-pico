import utime
from machine import Pin


class MotionSensorReader:
    """ core class to read the motion sensor values """

    def __init__(self, data_pin: int):
        """
        init function
        :param data_pin: GPIO number where the OUT is plugged
        """
        self._digital_val = Pin(data_pin, Pin.IN, Pin.PULL_UP)
        utime.sleep(3)

    def is_detected(self) -> int:
        """
        read the digital value of the motion sensor, 1 is a detected motion and 0 means no detection
        """

        return self._digital_val.value()
