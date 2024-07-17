import datetime

p= "My age is {0}, and I am still an {1}".format(20, "intern")  #string formating

print(p)

t = (1, 45,95, 0)

def minmax(t):
    return min(t), max(t)

print(minmax(t))

minimum, maximum = minmax(t)    #tuple unpacking

print("Minimum number from the tuple",t,"is",minimum,"and maximum number is",maximum)


#use of fstring

value = "Abdullah"

print(f"My name is {value}")


print(f"The current time is {datetime.datetime.now().isoformat()}") #isofomat function is used to change the time in internationally accepted format


#range
ran= range(0,6)
for i in ran:
    print(i)

list = (range(1, 11))

for k in enumerate(list):
    print(k)
