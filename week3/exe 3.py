class car:
    def __init__(self,make):
        self.make = make
    def runmake (self):
        return self.make
    
c1 = car('BMW')
print(c1.runmake())