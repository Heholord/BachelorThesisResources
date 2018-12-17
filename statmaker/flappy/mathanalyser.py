from flappy.splitter import *
from statistics import median, stdev


def print_run_stats(runNr, generations):
    count = 0
    for index, generation in enumerate(generations.values()):
        count += generation.genomecount()

    print("\t run count of run" + str(runNr) +"=" + str(count))
    return count


def print_goal_stats(runNr, generations):
    count = -1
    for index, generation in enumerate(generations.values()):
        if generation.maxFitness() > 600:
            count = generation.nr
            break

    print("\t goal reached in first " + str(count/len(generations)*100) + " % in run " + str(runNr))
    return count/len(generations) * 100


def print_score_stats(runNr, generations):
    score = 0
    for index, generation in enumerate(generations.values()):
        score += generation.fitness() / generation.genomecount()

    print("\t Avg score of run" + str(runNr) +"=" + str(score/len(generations)))
    return score/len(generations)


def print_distance_stats(runNr, generations):
    distance = 0
    for index, generation in enumerate(generations.values()):
        this_distace = generation.maxFitness() - median(list(map(lambda species: species.fitness()/species.genomecount(), generation.sortedListOfSpecies())))
        distance += this_distace

    print("\t Avg distance of run" + str(runNr) +"=" + str(distance/len(generations)))
    return distance/len(generations)


def print_regress_stats(runNr, generations):
    regress = 0
    count = 0
    for index, generation in enumerate(generations.values()):
        if index > 1:
            regress_value = generation.maxFitness() - generations[index-1].maxFitness()
            regress += min([0, regress_value])
            if regress_value < 0:
                count += 1
    print("\t Avg regress of run" + str(runNr) + "=" + str(regress / len(generations)) + " count:" + str(count))
    return regress / len(generations)


def print_success_stats(runNr, generations):
    success = 0
    for index, generation in enumerate(generations.values()):
        if index > 1:
            success += generation.maxFitness() - generations[index - 1].maxFitness()
    print("\t Avg success of run" + str(runNr) + "=" + str(success / len(generations)))
    return success / len(generations)


def print_all(popCount):
    print("\n\n\n--------------------" + str(popCount) + "--------------------")
    runcountList = []
    distance_list = []
    goalList = []
    regressList = []
    scoreList = []
    successList = []
    for i in range(1, 4):
        generations = getGenerations(popCount, i, False)
        runcountList.append(print_run_stats(i, generations))
        scoreList.append(print_score_stats(i, generations))
        distance_list.append(print_distance_stats(i, generations))
        regressList.append(print_regress_stats(i, generations))
        successList.append(print_success_stats(i, generations))
        goal = print_goal_stats(i, generations)
        if goal > 0:
            goalList.append(goal)
        print("")

    print("Avg run count of pop" + str(popCount) + "=" + str(sum(runcountList) / len(runcountList)) + " standard deviation " + str(stdev(runcountList)))
    print("Avg score of pop" + str(popCount) + "=" + str(sum(scoreList) / len(scoreList)) + " standard deviation " + str(stdev(scoreList)))
    print("goal reached in first " + str(sum(goalList) / len(goalList)) + "%; standard deviation " + str(stdev(goalList)))
    print("Avg distance of pop" + str(popCount) + "=" + str(sum(distance_list) / len(distance_list)) + " standard deviation " + str(stdev(distance_list)))
    print("Avg regress of pop" + str(popCount) + "=" + str(sum(regressList) / len(regressList)) + " standard deviation " + str(stdev(regressList)))
    print("Avg success of pop" + str(popCount) + "=" + str(sum(successList) / len(successList)) + " standard deviation " + str(stdev(successList)))


def print_overall_run_stats():
    pops = [10, 50, 250]
    runs = []

    print("\n\n\n-------------------------------------------------")
    print("\n--------------------run stats--------------------")
    for pop_nr in pops:
        for i in range(1, 4):
            generations = getGenerations(pop_nr, i, False)
            runs.append(print_run_stats(i, generations))

    print("Avg run count " + str(sum(runs) / len(runs)) + " standard deviation " + str(stdev(runs)))


print_all(10)
print_all(50)
print_all(250)

print_overall_run_stats()
