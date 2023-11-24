class Rooms:

    def __init__ (self):
        self.features=[]
        self.clues=[]
    
    def addFeatures(self,feature):
        self.features.append(feature)
    
    def printStuff(self):
        for x in self.features:
            print(x)
        for x in self.clues:
            print(x)
        
    def addClues(self,clue):
        self.clues.append(clue)
    

Room1=Rooms()
Room1.addFeatures("table")
Room2=Rooms()
Room2.addFeatures("clock")
Room1.addClues("bible in draw")
Room1.addClues("mirror")
Room2.addClues("clock shows 13F")
Room1.printStuff()
Room2.printStuff()
