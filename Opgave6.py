class Exercise6:
    _input = 0

    def __input(self):
        self._input = input("Please insert a number")

    def __readinput(self):
        if (int(self._input)%2) == 0:
            print("It's an even number")
        else:
            print("it's an uneven number")

    def run(self):
        self.__input()
        self.__readinput()