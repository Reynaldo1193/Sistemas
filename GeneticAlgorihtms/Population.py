#coding=utf-8

import DNA

target = "To be or not to be"

class Population():
    """docstring forPopulation."""
    def __init__(self,target):
        self.population = []
        populationSize = 50
        for i in range(0,populationSize):
            self.population.append(DNA.DNA(len(target)))

poblacion = Population(target)
print(poblacion.population[10].genes)
