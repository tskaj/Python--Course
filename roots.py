def sqrt(x):
    """Computes square roots using
    the method of Heron of Alexandria
    """

    guess = x 
    i=0
    try:
        while guess*guess!= x and 1< 20:
            guess = (guess+x/guess)/2.0
            i+=1

    except ZeroDivisionError:
            raise ValueError()
    
    return guess

def main():
    print(sqrt(9))
    print(sqrt(2))
    print(sqrt(-1))
if __name__== "__main__":
    main()