#If statements
if True:
    print ("its true")

if (bool("eggs")):
    print("yes! please")

if "eggs":
    print("yes!pleas")

h = 42

if h > 50:
    print ("Greater than 50")
else:
    print("smaller than 50")

a= 100

if a<50:
    print("smaller than 100")
elif a==100:
    print("equal  to 100")
else: 
    print ("greater than hundered")

while a!=90:    #while loop
    print (a)
    a-=1

# while True: 
 #   pass    #press ctrl c to get out of the loop

while True:
    response = input()
    if int(response)%7==0:
        break