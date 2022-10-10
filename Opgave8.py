class Exercise8:

    _list = []
    _inputX = None

    def __EnterNumberInList(self):
        _inputX = input("Please insert a number or enter quit: ")
        if _inputX == "quit":
            print("Program Ended")
            print(self._list)
        else:
            while _inputX != "quit":
                if int(_inputX) > 0:
                    print("You have entered a positive number: " + _inputX)
                    self._list.append(int(_inputX))
                elif int(_inputX) == 0:
                    print("You have entered: " + _inputX)
                    self._list.append(int(_inputX))
                else:
                    print("You have entered a negative number: " + _inputX)
                    self._list.append(int(_inputX))
                print(str(self._list) + "\n")
                _inputX = input("Please insert a number")

    def run(self):
        self.__EnterNumberInList()