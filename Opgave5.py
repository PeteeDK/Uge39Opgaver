class Exercise5:

    data = [65,81,43,63,27,69,43,68,88,76,30,99,74,11,89,38,73,9]
    '''
    def FindTheAverageOfData(self):
        total = 0
        amount = 0
        higestNrInList = 0

        for x in self.data:
            total += x
            amount = amount + 1
        print("The sum of the list is: " + str(total/amount))
    '''

    def sum (self):
        x = sum(self.data)
        print("This is the sum of the list: " + str(x))


    def FindHigstNrInList(self):
        number :int = 0
        for x in self.data:
            if number <= x:
                number: int = x
        return number

    def PrintHigestNumber(self):
        print("This is the higst number in the list: " + str(self.FindHigstNrInList()))


    def PositionOfHigstNr(self):
        index = self.data.index(self.FindHigstNrInList())
        print("This is the position of the higest number in the array: " + str(index))

    def PrintNumbersBetween(self):
        higestnumber = []
        for x in self.data:
            if x >= 40 and x <= 70:
                higestnumber.append(x)
        print("This is the the numbers between 40 and 70: " + str(higestnumber))

class Exercise5b:
    _amountOfNumberInList = 0
    _numberToAddToList =0
    _list = []

    def __ChooseAmoutOfNrToList(self):
        self._amountOfNumberInList = int(input("How many numbers do you want to put together: "))
        self._list = self._list * self._amountOfNumberInList


    def __AddNumberToList(self):
        while len(self._list) < self._amountOfNumberInList:
            self._numberToAddToList = int(input("Please enter a number"))
            self._list.append(self._numberToAddToList)

    def __printList(self):
        print(self._list)


    def __sum(self):
        x = sum(self._list)
        print("This is the sum of the list: " + str(x))



    def run(self):
        self.__ChooseAmoutOfNrToList()
        self.__AddNumberToList()
        #self.__printList()
        self.__sum()




