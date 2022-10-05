class Opgave1:
    _firstNr =  0
    _secondNr = 0

    def __EnterNr(self):
        self._firstNr = input("Please enter the first number")
        self._secondNr = input("Please enter the second number")

    def __Average(self):
        average = (int(self._firstNr) + int(self._secondNr)) / 2
        print("This is the average: " + str(average))

    def Run(self):
        self.__EnterNr()
        self.Average()

