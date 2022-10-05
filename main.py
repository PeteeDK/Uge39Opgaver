import Opgave1
import Opgave2
import Opgave3
import Opgave4
import Opgave5
import OpgaveCounter

'''
number1 = int(input("number1"))
number2 = int(input("number2"))

avarge = (number1+number2)/2
print(avarge)
'''

newCounter = OpgaveCounter.Counter()
newCounter.count()
newOpgave1 = Opgave1.Opgave1()
newOpgave1.Run()
#newOpgave1.EnterNr()
# newOpgave1.Average()
#newOpgave1.Run()

newCounter.count()
newOpgave2 = Opgave2.Exercise2()
# newOpgave2.EnterSize()
# newOpgave2.PrintRoomArea()

newCounter.count()
newOpgave3 = Opgave3.Exercise3()
# newOpgave3.EnterTemp()
# newOpgave3.PrintOutTemp()

newCounter.count()
newOpgave4 = Opgave4.Exercise4()
# newOpgave4.EnterNrOfDays()
# newOpgave4.MounthGuesser()

newCounter.count()
newOpgave5 = Opgave5.Exercise5()

newOpgave5.FindTheAverageOfData()
newOpgave5.FindHigstNrInList()
#newOpgave5.PrintHigestNumber()
newOpgave5.PositionOfHigstNr()
# newOpgave5.PrintNumbersBetween()

newOpgave5b = Opgave5.Exercise5b()
#newOpgave5b.ChooseAmoutOfNrToList()
#newOpgave5b.AddNumberToList()
