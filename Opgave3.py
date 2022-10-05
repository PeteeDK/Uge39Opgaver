class Exercise3:
    temp : int = 0

    def EnterTemp(self):
        self.temp = int(input("Please enter the temperature"))
        return int(self.temp)

    def PrintOutTemp(self):
        if self.temp <= 0:
            print("Warning: Low temperatur")
        elif self.temp <= 34:
            print("Temperatur is okay")
        else:
            print("Warning: temperatur too HIGH!")
