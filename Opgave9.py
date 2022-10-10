class Exercise9:

    _number1 = 0
    _number2 = 0
    _number3 = 0
    _list = []

    def Run(self):
        self.__InsertnumberToList()
       # self.__sortListWithSort()
        self.__sortList()
       # self.__PrintList()

    def __InsertnumberToList(self):
        self._number1 = int(input("Enter a number"))
        self._list.append(self._number1)
        self._number2 = int(input("Enter a number"))
        self._list.append(self._number2)
        self._number3 = int(input("Enter a number"))
        self._list.append(self._number3)

    #Easy way so sort from smallest to largest
    def __sortListWithSort(self):
        self._list.sort()

    def __sortList(self):
        mimimum = min(self._list)
        maximum = max(self._list)
        middle = sum(self._list) - mimimum - maximum

        print("This is the smallest: " + str(mimimum))
        print("This is the middle: " + str(middle))
        print("This is the largest: " + str(maximum))

    def __PrintList(self):
        print(self._list)
