import time


class timer:
    def __init__(self, minutes=int(0), seconds=float(0)):
        self.seconds = float(seconds)
        self.minutes = int(minutes)
        self.hours = int(0)

    def __timeUP(self):
        if (self.hours == 0 and self.minutes == 0 and round(self.seconds, 2) == 0.00):
            return True
        else:
            return False

    # decrement cannot take any arguments. Because it is not available for user.
    def __decrement(self):
        if self.__timeUP():
            raise StopIteration('Seconds < 0')

        if self.seconds < 0.00:
            self.seconds = 60
            self.minutes -= 1

        time.sleep(0.01)
        self.seconds -= 0.01

    def Start(self, console=False):  # Capital 'S' means user function.
        if self.__timeUP():
            print("Timer not set")
            return

        while (not self.__timeUP()):
            print("Working: ", self, end="\r")
            self.__decrement()

        print(self, "Time's up \a")

    def __str__(self):
        return "{:02d}:{:02d}:{:05.2f}".format(self.hours, self.minutes, self.seconds)


if __name__ == "__main__":

    timerObject = timer(0, 10)
    print("Timer: ", timerObject)

    start = input("Start (y/n): ")

    if start.lower() == 'y':
        try:
            timerObject.Start()
        except KeyboardInterrupt:
            print("But why at", timerObject, "?")
    else:
        print("Good luck!")
