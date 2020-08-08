import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    three_same_drawn = 0
    for i in range(numTrials):
        bucket = ["g", "g", "g", "r", "r", "r"]
        for i in range(3):
            bucket.pop(random.randint(0, 5-i))
        
        if bucket[0] == bucket[1] and bucket[1] == bucket[2]:
            three_same_drawn += 1

    return three_same_drawn / numTrials
