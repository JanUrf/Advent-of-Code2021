from lanternfish import Lanternfish

def main():
    input_data = importData('input')
    population = []
    for start_value in input_data:
        population.append(Lanternfish(start_value))
    for j in range (0,80):
        new_population = []
        for i in population:
            new_fish = i.decrease()
            new_population.append(i)
            if new_fish is not None:
                new_population.append(new_fish)
        population = new_population
        print(len(population))

        #print_population(population)


def print_population(pop):
    print(",".join(str(o.get_timer()) for o in pop))


def importData(path):
    with open(path) as f:
        data = [int(s) for s in f.readlines()[0].split(',')]
    return data

if __name__ == '__main__':
    main()
