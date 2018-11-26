#coding=utf-8

import random as rand
def newChar ():
    c = rand.randint(32,122)
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
