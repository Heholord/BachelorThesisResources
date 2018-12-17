import matplotlib.pyplot as plt
from mario.splitter import *


def print_for_generations(popCount, runNr):
    data = []
    columns = []
    rows = []

    generations = getGenerations(popCount, runNr, False)

    skipRatio = len(generations)//30
    skipRatio = 1 if skipRatio == 0 else skipRatio
    pos = range(0, len(generations), skipRatio)

    for index, generation in enumerate(generations):
        rows.append(generation.maxFitness())
        columns.append(generation.nr)

        if index % skipRatio == 0:

            rowData = []
            for population in generation.species:
                rowData.append(population.fitness() / population.genomecount())
            data.append(rowData)

    plt.locator_params(axis='x', nbins=10)
    plt.tick_params(axis='x', pad=skipRatio)
    plt.title("Population " + str(popCount) + ", run " + str(runNr))
    plt.xlabel("Generation")
    plt.ylabel("Avg Fitness per Species")
    plt.ylim(-100, 4800)
    plt.boxplot(data, manage_xticks=False, positions = pos, widths=(skipRatio*0.8))
    plt.plot(columns, rows)
    plt.tight_layout()
    plt.savefig("mario/plts/pop" + str(popCount) + "_run" + str(runNr)+".png", dpi=300)
    plt.close()
    # plt.show()



print_for_generations(10, 1)
print_for_generations(10, 2)
print_for_generations(10, 3)
print_for_generations(50, 1)
print_for_generations(50, 2)
print_for_generations(50, 3)
print_for_generations(250, 1)
print_for_generations(250, 2)
print_for_generations(250, 3)
