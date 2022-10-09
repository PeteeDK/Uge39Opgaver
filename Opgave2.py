class Exercise2:
    length = 0
    width = 0

    def EnterSize(self):
        self.length = input("Please enter the length of the room in meters: ")
        self.width = input("Please enter the width of the room in meters: ")

    def AreaOfRoom(self):
        area = int(self.length)*int(self.width)
        return area

    def PrintRoomArea(self):
        print("The area of the room is: " + str(self.AreaOfRoom()) + "m")