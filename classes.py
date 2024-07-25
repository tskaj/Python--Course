'''class Person:
    def __intit__(self, name, age, string):
        self.name = name
        self.age = age
        self.designation = string

p1 = Person()


print(f"I'm an {p1.designation} at EMUMBA Private limmited")
print(p1.name)

print(p1.age)
'''

class Person:
  def __init__(self, name, age, string):
    self.name = name
    self.age = age
    self.string = string

  def myfunc(self):
    print("Hello my name is " + self.name + ", And I am an "+self.string+" here at Emumba Private Limmitted")

p1 = Person("John", 36, "Intern")
p1.myfunc()
