import matplotlib.pyplot as plt
from flappy.splitter import *


def print_for_generations(popCount, runNr):
    data = []
    columns = []
    rows = []

    generations = getGenerations(popCount, runNr, False)

    skipRatio = len(generations)//30
    skipRatio = 1 if skipRatio == 0 else skipRatio
    pos = range(1, len(generations)+1, skipRatio)

    for (index, generation) in enumerate(generations):
        rows.append(generations[generation].maxFitness())
        columns.append(generation)

        if index % skipRatio == 0:
            rowData = []
            for population in generations[generation].species:
                rowData.append(population.fitness() / population.genomecount())
            data.append(rowData)

    fig1, ax1 = plt.subplots()
    ax1.locator_params(axis='x', nbins=10)
    ax1.tick_params(axis='x', pad=skipRatio)



    # plt.subplot(211)
    plt.title("Population " + str(popCount) + ", run " + str(runNr))
    plt.xlabel("Generation")
    plt.ylabel("Avg Fitness per Species")
    ax1.set_yscale('log')
    plt.ylim(1, 1500)
    ax1.boxplot(data, manage_xticks=False, positions=pos, widths=(skipRatio * 0.8))
    ax1.plot(columns, rows)

    # plt.subplot(212)
    # plt.xlabel("Generation")
    # plt.ylabel("Avg Fitness per Species")
    # plt.ylim(-50, 115)
    # plt.boxplot(data, manage_xticks=False, positions=pos, widths=(skipRatio * 0.8))

    plt.tight_layout()
    # plt.savefig("plts/pop" + str(popCount) + "_run" + str(runNr) + ".png", dpi=300)
    # plt.close()
    plt.show()


print_for_generations(10, 1)
print_for_generations(10, 2)
print_for_generations(10, 3)
print_for_generations(50, 1)
print_for_generations(50, 2)
print_for_generations(50, 3)
print_for_generations(250, 1)
print_for_generations(250, 2)
print_for_generations(250, 3)
