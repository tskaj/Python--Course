x =25
def square(x):
    return 25*25

def launch_missles():
    print("Nuclear Missle has been Launched!")

print(launch_missles())


def factorial(n):           #user Defined Factorial function using recursion method
    if (n==0):
        return 1
    else:
        return n* factorial(n-1)

print(factorial(5))