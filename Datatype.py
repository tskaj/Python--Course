print (int ("32")) #typecasting string into integer

a = 10
x = 0b10    #10 stored in binary
y = 0o10    #10 stored in octal 
z = 0x10    #10 stored in hexadecimal

print(a, x, y, z)

speed_of_light = 3e8

print("Speed of light is equal to",speed_of_light)

Planks_const = 1.616e-35

print("Plank's constant is equal to",Planks_const)

Product = speed_of_light* Planks_const

print ("Their product is equal to", Product)

print(int(Product)) #This will print 0

b= None

print(b is None) #is operator

print (float(3)) #This will print 3.0

print(bool([])) #False

print (bool([1, 2, 3])) #true

d = b'some bytes'
print(d[0])

print (d.split())


#lists
l = [1,9,3]
print (l)

fruits = ["apple", "banana", "pineapple"]

print(fruits[2])

new = []
new.append("entry to the last in the list")
print(new)

print(list("characters"))


#Dictionaries

dic = {"Abdullah" : "03165325478", "Javed": "03336857513", 2 : 5}