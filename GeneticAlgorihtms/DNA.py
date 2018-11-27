#coding=utf-8

from random import randint
def newChar ():
    c = randint(32,122)
    return chr(c)

class DNA:
    """docstring forDNA."""
    def __init__(self, num):
        self.genes = []
        self.fitness = 0
        for i in range(0,num):
            self.genes.append(newChar())

    def getPhrase(self):
        phrase = "".join(self.genes)
        return phrase

    def calcFitness(self,target):
        self.score = 0
        self.fitness = 0.0
        self.targetSize = len(target)
        for i in range(0,self.targetSize):
            if(self.genes[i] == target[i]):
                self.score = self.score+1
        self.fitness =  float(self.score)/float(self.targetSize)

    def crossover(self,partner):
        child = DNA(len(self.genes))
        midpoint = randint(0,len(self.genes)-1)

        for i in range(0,len(self.genes)):
            if(i>midpoint):
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child



        print(len(self.genes))
        print(midpoint)
