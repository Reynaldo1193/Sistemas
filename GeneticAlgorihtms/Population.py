#coding=utf-8

import DNA

populationSize = 10
target = "To be or not to be"

class Population():
    """docstring forPopulation."""
    def __init__(self,target):
        self.population = []
        for i in range(0,populationSize):
            self.population.append(DNA.DNA(len(target)))

    def calcFitness(self):
        for i in range(0,populationSize):
            self.population[i].calcFitness(target)
            print(self.population[i].getPhrase())

poblacion = Population(target)
poblacion.calcFitness()
