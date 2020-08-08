def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    x = 0
    while True:
        if test(x):
            return x
        elif test(-x):
            return -x
        x += 1


#### This test case prints 80 ####
def f(x):
    return x == -80


print(solveit(f))
