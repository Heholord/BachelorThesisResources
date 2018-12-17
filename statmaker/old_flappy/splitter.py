from old_flappy.generation import *


def getGenerations(popCount, ratio, run, shouldPrint):

    # statisticFiles = []
    #
    # os.chdir(".")
    # for file in glob.glob("*.txt"):
    #     statisticFiles.append(file)
    #     print(file)

    f = open("pop" + str(popCount) + "_ratio" + str(ratio) + "_run" + str(run) + ".txt", "r")
    lines = f.readlines()
    f.close()

    generations = []

    def getLast(list):
        return list[len(list) - 1]

    for line in lines:
        line = line.strip()
        line = line.replace("Gen ", "")
        line = line.replace("species ", "")
        line = line.replace("fitness ", "")
        line = line.replace("score ", "")
        line = line.split(" ")
        generationNr = int(line[0])
        speciesNr = int(line[1])
        fitness = float(line[2])
        fitness = fitness if fitness > 0 else 0
        score = int(line[3])

        if len(generations) == 0 or getLast(generations).nr != generationNr:
            lastGeneration = Generation(generationNr, [])
            generations.append(lastGeneration)

        lastGeneration.addSpecies(Species(speciesNr, fitness))

    if shouldPrint:
        for generationElem in generations:
            print(str(generationElem.nr) + ": " + str(generationElem.fitness()/generationElem.speciescount()))
            for species in generationElem.species:
                print("\t\t" + str(species.nr) + ": " + str(species.fitness()))

    return generations
