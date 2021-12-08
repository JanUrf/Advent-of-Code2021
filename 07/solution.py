import numpy as np
import math

def main(exp_growth):
    data = import_data()
    costs = []
    # calculate all positions
    for i in range(0, np.amax(data) + 1):
        # for second parse use True for exp growing
        costs.append(calculate_fuel(data, i, exp_growth))
    # search for minimal position
    position_min_costs = costs.index(min(costs))
    print('The position with the minimal costs of %d is position %d' %(costs[position_min_costs], position_min_costs))


def main2(exp_growth):
    data = import_data()
    if exp_growth == True:
        target = math.floor(np.mean(data))
    else:
        target = np.median(data)
    costs = calculate_fuel(data, target, exp_growth)
    print('The position with minimal costs of %d is position %d' %(costs, target))

def import_data():
    with open('input') as f:
       data = np.array([int(s) for s in f.readlines()[0].split(',')])
    return data

def calculate_fuel(positions, target, exp=False):
    target_vector = np.array([target] * positions.size)
    difference = np.abs(positions - target_vector)
    # if the costs don't grow linear use a mapping
    if exp == True:
        difference = summenformel(difference)
    return np.sum(difference)

# Gausssche Summenformel
def summenformel(n):
    return n*(n+1)/2


if __name__ =='__main__':
    exponental_growth = False
    print('Numerical approach:')
    main(exponental_growth)
    print('Efficient approach:')
    main2(exponental_growth)
