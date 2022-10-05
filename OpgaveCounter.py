class Counter:
    opgaveCounter : int = 0

    def count(self):
        self.opgaveCounter += 1
        print("\n"+"This is Exercise Nr: "+str(self.opgaveCounter))
