import numpy as np, itertools

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """

    #Finds a combination of integers that fufill the total or is closest combination of integers less than the total
    best = [0]
    found = False
    for i in range(1, len(choices) + 1):
        if found:
            break
        combos = list(itertools.combinations(choices, i))
        for k in combos:
            if sum(k) == total:
                best = k
                found = True
                break
            elif sum(k) < total and sum(k) > sum(best):
                best = k

    #Creates binary representation of inputted list on whether each integer is used
    binary = []
    best = list(best)
    for num in choices:
        if num in best:
            binary.append(1)
            best.remove(num)
        elif len(best) == 0:
            break
        else:
            binary.append(0)

    #Fills rest of the binary list with 0s if all numbers are that are used in best are filled with 1s before previous loop gets to the end of choices
    while len(binary) < len(choices):
        binary.append(0)

    return np.array(binary)
    
            
print(find_combination([4, 6, 3, 5, 2], 10))