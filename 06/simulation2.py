import numpy as np

def main():
    n = 80
    input_data = np.array(importData('input'))
    for i in range (0,n):
        input_data -= 1
        # count how many fishes creates a new fish
        new_fishes_nr = np.count_nonzero(input_data < 0)
        # creating new fishes and append them to the population
        input_data = np.append(input_data, [8] * new_fishes_nr)
        # refresh the timer to 6
        input_data[input_data < 0] = 6
        print('After \t %d days the population size is: %d' %(i+1, input_data.size))


def importData(path):
    with open(path) as f:
        data = [int(s) for s in f.readlines()[0].split(',')]
    return data

if __name__ == '__main__':
    main()
