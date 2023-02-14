import utime

from motion_sensor import MotionSensorReader


class Main:
    """ main class that will handle the loop """

    def __init__(self):
        """
        init function
        """
        self._motion = MotionSensorReader(data_pin=0)

    def run(self) -> None:
        """
        core function to iterate
        For each iteration the motion value will be read
        """
        while True:
            print(f"is detected: {self._motion.is_detected()}")
            utime.sleep(0.5)


if __name__ == '__main__':
    run = Main()
    run.run()
