class Exercise4:
    numberOfDays = 0

    def EnterNrOfDays(self):
        self.numberOfDays = int(input("Please enter Nr of days"))
        return self.numberOfDays

    def MounthGuesser(self):
        if self.numberOfDays == 28 or self.numberOfDays == 29:
            print("Feb")
        elif self.numberOfDays == 30:
            print("Apr, Jun, Sep, Nov")
        elif self.numberOfDays == 31:
            print("Jan, Mar, May, Jul, Aug, Oct, Dec")
        else:
            print("Error")

    def PrintNrOfDaysEntered(self):
        print(self.numberOfDays)