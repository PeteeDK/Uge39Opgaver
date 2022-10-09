class Exercise3:
    temp : int = 0

    def EnterTemp(self):
        self.temp = int(input("Please enter the temperature"))
        return int(self.temp)

    def PrintOutTemp(self):
        if self.temp <= 0:
            print("Warning: Low temperature")
        elif self.temp <= 34:
            print("Temperature is okay")
        else:
            print("Warning: Temperature too HIGH!")
