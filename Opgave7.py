import random

class Exercise7:

    _randomNumber1 = 0
    _randomNumber2 = 0
    _randomNumber3 = 0
    _answerlist = []
    _answer = 0
    _x = -1

    _problemNumber = 0

    #
    def problemNumber(self):
        self._problemNumber +=1
        return self._problemNumber


    def randomNumberGen (self):
        self._randomNumber1 = random.randrange(20, 50)
        self._randomNumber2 = random.randrange(20, 50)
        self._randomNumber3 = random.randrange(20, 50)

    def creatProblem(self):
        a = self._randomNumber1
        b = self._randomNumber2
        c = self._randomNumber3
        print("This is problem nr: " + str(self.problemNumber()) + "\n"
              + str(a) + " + " + str(b) + " + " + str(c))
        answer = a+b+c
        #print("CheatCheet: " +str(answer))
        #print("Answer + 5: " + str(answer + 5))
        #print("Answer - 5: " + str(answer - 5))
        self._answerlist.append(answer)

    def Anwser (self):
        self._answer = input("Please answer the question: ")

    def answerTest(self):
        self._x += 1
        if int(self._answer) == self._answerlist[self._x]:
            print("Correct Answer \n")
        elif self._answerlist[self._x] - 5 <= int(self._answer):
            if self._answerlist[self._x] + 5 >= int(self._answer):
                print("So Close \n")
            else:
                print("Wrong answer \n")
        else:
            print("Wrong answer \n")

    def createList(self):
        while len(self._answerlist) <= 9:
            self.randomNumberGen()
            self.creatProblem()
            self.Anwser()
            self.answerTest()

    def prinList(self):
        print(self._answerlist)
