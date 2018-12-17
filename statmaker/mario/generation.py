class Generation:
    def __init__(self, generationNr, species):
        self.species = species
        self.nr = generationNr

    def addSpecies(self, species):
        self.species.append(species)

    def getSpecies(self, nr):
        for speciesEl in self.species:
            if(speciesEl.nr == nr):
                return speciesEl
        return None

    def addSpeciesGenome(self, speciesNr, genome):
        speciesEntry = self.getSpecies(speciesNr)
        if speciesEntry is None:
            speciesEntry = Species(speciesNr, [])
            self.addSpecies(speciesEntry)
        speciesEntry.addGenome(genome)

    def fitness(self):
        return sumFitness(self.species)

    def genomecount(self):
        return sumGenome(self.species)

    def maxFitness(self):
        return maxfitness(self.species)

    def sortedListOfSpecies(self):
        return sorted(self.species, key=lambda species: species.fitness())

class Species:
    def __init__(self, speciesNr, genome):
        self.genome = genome
        self.nr = speciesNr

    def addGenome(self, genome):
        self.genome.append(genome)

    def fitness(self):
        return sumFitness(self.genome)

    def genomecount(self):
        return sumGenome(self.genome)

    def maxFitness(self):
        return maxfitness(self.genome)


class Genome:
    def __init__(self, genomeNr, fitness):
        self.nr = genomeNr
        self.fitnessVar = fitness

    def fitness(self):
        return self.fitnessVar

    def maxFitness(self):
        return self.fitnessVar

    def genomecount(self):
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

def sumGenome(genomeContainers):
    sumGenome = 0
    for genome in genomeContainers:
        sumGenome += genome.genomecount()
    return sumGenome