class Exercise10:
    _list = []
    _input = None

    def _addNumberToList(self):
        _input = int(input("Please insert a number or 0 to end program"))
        while _input != 0:
            self._list.append(_input)
            _input = int(input())
        else:
            self._list.sort()
            for x in self._list:
                print(x)


    def Run(self):
        self._addNumberToList()
