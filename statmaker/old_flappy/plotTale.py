import matplotlib.pyplot as plt
from old_flappy.splitter import *


def print_for_generations(generations, label):
    data = []
    columns = []
    rows = []

    for generation in generations:
        rows.append(generation.maxFitness())
        columns.append(generation.nr)

    for generation in generations:
        rowData = []
        for population in generation.species:
            rowData.append(population.fitness())
        data.append(rowData)

    plt.locator_params(axis='x', nbins=10)
    plt.title(label)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.ylim(-10, 2000)
    plt.boxplot(data, manage_xticks=False)
    plt.plot(columns, rows)
    plt.show()


print_for_generations(getGenerations( 10, 40, 1, False), "Population 10, best 40% reproduce, run 1")
print_for_generations(getGenerations( 50,  4, 1, False), "Population 50, best 4% reproduce, run 1")
print_for_generations(getGenerations( 50, 10, 1, False), "Population 50, best 10% reproduce, run 1")
print_for_generations(getGenerations( 50, 10, 2, False), "Population 50, best 10% reproduce, run 2")
print_for_generations(getGenerations( 50, 10, 3, False), "Population 50, best 10% reproduce, run 3")
print_for_generations(getGenerations( 50, 40, 1, False), "Population 50, best 40% reproduce, run 1")
print_for_generations(getGenerations( 50, 40, 2, False), "Population 50, best 40% reproduce, run 2")
print_for_generations(getGenerations( 50, 40, 3, False), "Population 50, best 40% reproduce, run 3")
print_for_generations(getGenerations(250,  1, 1, False), "Population 250, best 0.8% reproduce, run 1")
print_for_generations(getGenerations(250,  4, 1, False), "Population 250, best 4% reproduce, run 1")
print_for_generations(getGenerations(250, 10, 1, False), "Population 250, best 10% reproduce, run 1")
print_for_generations(getGenerations(250, 10, 2, False), "Population 250, best 10% reproduce, run 2")
print_for_generations(getGenerations(250, 40, 1, False), "Population 250, best 40% reproduce, run 1")
print_for_generations(getGenerations(250, 40, 2, False), "Population 250, best 40% reproduce, run 2")
