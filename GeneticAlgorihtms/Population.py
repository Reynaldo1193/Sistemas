#coding=utf-8

import DNA
from random import randint
populationSize = 50
target = "To be or not to be"

class Population():
    """docstring forPopulation."""
    def __init__(self,target):
        self.population = []
        self.matingPool = []
        self.perfectScore = 1
        self.generations = 0

        for i in range(0,populationSize):
            self.population.append(DNA.DNA(len(target)))

    def calcFitness(self):
        for i in range(0,populationSize):
            self.population[i].calcFitness(target)

    def naturalSelection(self):
        self.matingPool = []
        maxFitness = float(0);
        n=float(0)
        for i in range(0,len(self.population)):
            if(maxFitness < self.population[i].fitness):
                maxFitness = self.population[i].fitness

        for i in range(0,len(self.population)):
            if(maxFitness>0):
                n = int(float(self.population[i].fitness/maxFitness)*100)
                for j in range(0,n):
                    self.matingPool.append(self.population[i])
            else:
                self.matingPool.append(self.population[i])


    def generate(self):
        for i in range(0,populationSize):
            a = randint(0,len(self.matingPool)-1)
            b = randint(0,len(self.matingPool)-1)
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            child = partnerA.crossover(partnerB)
            self.population[i] = child

        self.generations = self.generations+1

poblacion = Population(target)
for i in range(0,10):
    poblacion.calcFitness()
    poblacion.naturalSelection()
    poblacion.generate()
    print("iteracion "+str(i))
    for j in range(0,len(poblacion.population)):
        print(poblacion.population[j].getPhrase())
