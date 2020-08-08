import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    rabbit_pop = CURRENTRABBITPOP
    for i in range(rabbit_pop):
      if CURRENTRABBITPOP == MAXRABBITPOP:
        break
      reproduction_prob = 1 - CURRENTRABBITPOP/MAXRABBITPOP
      if random.random() <= reproduction_prob:
        CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    fox_pop = CURRENTFOXPOP
    for i in range(fox_pop):
      eat_prob = CURRENTRABBITPOP/MAXRABBITPOP
      if random.random() <= eat_prob and CURRENTRABBITPOP != 10:
        CURRENTRABBITPOP -= 1
        if random.random() <= 0.3:
          CURRENTFOXPOP += 1
      else:
        if CURRENTFOXPOP == 10:
          continue
        else:
          if random.random() <= 0.9:
            CURRENTFOXPOP -= 1
    

def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_pop = []
    fox_pop = []
    for i in range(numSteps):
      rabbitGrowth()
      foxGrowth()
      rabbit_pop.append(CURRENTRABBITPOP)
      fox_pop.append(CURRENTFOXPOP)
    
    pylab.figure()
    pylab.subplot(1,2,1)
    pylab.plot(range(1, numSteps + 1), rabbit_pop)
    coeff = pylab.polyfit(range(len(rabbit_pop)), rabbit_pop, 2)
    pylab.plot(pylab.polyval(coeff, range(len(rabbit_pop))))
    pylab.subplot(1,2,2)
    pylab.plot(range(1, numSteps + 1), fox_pop)
    coeff = pylab.polyfit(range(len(fox_pop)), fox_pop, 2)
    pylab.plot(pylab.polyval(coeff, range(len(fox_pop))))
    pylab.show()
    return rabbit_pop, fox_pop


runSimulation(200)
