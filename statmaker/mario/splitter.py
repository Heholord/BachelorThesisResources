from mario.generation import *


def getGenerations(popCount, run, shouldPrint):

    # statisticFiles = []
    #
    # os.chdir(".")
    # for file in glob.glob("*.txt"):
    #     statisticFiles.append(file)
    #     print(file)

    # f = open("mario/pop" + str(popCount) + "_run" + str(run) + ".txt", "r")
    f = open("pop" + str(popCount) + "_run" + str(run) + ".txt", "r")
    lines = f.readlines()
    f.close()

    generations = []

    def getLast(list):
        return list[len(list) - 1]

    for line in lines:
        line = line.strip()
        line = line.replace("Gen ", "")
        line = line.replace("species ", "")
        line = line.replace("genome ", "")
        line = line.replace("fitness: ", "")
        line = line.split(" ")
        generationNr = int(line[0])
        genomeNr = int(line[2])
        speciesNr = int(line[1])
        fitness = float(line[3])

        if len(generations) == 0 or getLast(generations).nr != generationNr:
            lastGeneration = Generation(generationNr, [])
            generations.append(lastGeneration)

        lastGeneration.addSpeciesGenome(speciesNr, Genome(genomeNr, fitness))

    if shouldPrint:
        for generationElem in generations:
            print(str(generationElem.nr) + ": " + str(generationElem.fitness()/generationElem.speciescount()))
            for genome in generationElem.genoms:
                print("\t" + str(genome.nr) + ": " + str(genome.fitness()/genome.speciescount()))
                for species in genome.species:
                    print("\t\t" + str(species.nr) + ": " + str(species.fitness()))

    return generations
