class Generation:
    def __init__(self, genNr, species):
        self.species = species
        self.nr = genNr

    def addSpecies(self, species):
        self.species.append(species)

    def fitness(self):
        return sumFitness(self.species)

    def speciescount(self):
        return sumSpecies(self.species)

    def maxFitness(self):
        return maxfitness(self.species)


class Species:
    def __init__(self, speciesNr, fitness):
        self.nr = speciesNr
        self.fitnessVar = fitness

    def fitness(self):
        return self.fitnessVar

    def maxFitness(self):
        return self.fitnessVar

    def speciescount(self):
        return 1


def maxfitness(fitnesses):
    max = 0.0
    for fitnessEntry in fitnesses:
        current = fitnessEntry.maxFitness()
        max = max if max > current else current
    return max


def sumFitness(fitnesses):
    sumFitness = 0.0
    for fitnessEntry in fitnesses:
        sumFitness = sumFitness + fitnessEntry.fitness()
    return sumFitness

def sumSpecies(speciesContainers):
    sumSpecies = 0
    for spieces in speciesContainers:
        sumSpecies += spieces.speciescount()
    return sumSpecies