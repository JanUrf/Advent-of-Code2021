import numpy as np

def main():
    n = 256
    # read input file
    with open('input') as f:
        data = np.array([int(s) for s in f.readlines()[0].split(',')])

    # initialize dictionary
    population = {}
    for i in range (0,9):
        population[i] = np.count_nonzero(data == i)

    for j in range (0,n):
        # initialize new population
        new_population = {value:0 for value in range(0,9)}
        for i in population.keys():
            # if the fish will produce a new fish
            if i == 0:
                new_population[6] += population[i]
                new_population[8] += population[i]
            # decrease the timer
            else:
                new_population[i-1] += population[i]

        population = new_population
        print('After \t %d days the population size is: %d' %(j+1, popsize(population)))

def popsize(pop):
    return sum(pop.values())

if __name__ == '__main__':
    main()
