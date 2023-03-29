#with open('python_test.py') as f:
#    for line in f:
#        print(line)


eh = (lambda x: x > 2)(3)
if eh:
    print('oy')

def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_5 = create_adder(5)

x = map(add_5, [1,2,20,200])

for y in x:
    print(y)


a = filter(lambda y: y % 3 == 0, x)

for b in a:
    print(b)

c = [add_5(i) for i in range(10)]
print(c)

# local file has priority over python built-in libraries

#sub class from object to get a class
class Human(object):
    # class attribute shared by all instances of this class
    species = "Homo Spaiens"

    # Called when the class is instantiated.
    # __.. attributes/objects used by Python but live in user-controlled namespaces.
    # Should not be redeclared.
    def __init__(self, name):
        self.name = name

        self.age = 0

    def say(self,msg):
        return "{}: {}".format(self.name, msg)

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        return "grunttt"
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age
        
    
# Instantiate a class
i = Human(name="Ian")
print(i.say("hi"))  # prints out "Ian: hi"

j = Human("Joel")
print(j.say("hello"))  # prints out "Joel: hello"


print(i.get_species())
print(j.get_species())

Human.species = 'cuthululu'

print(i.get_species())
print(j.get_species())

# does not work.. class level var
i.species = 'the fuck'
print(i.get_species())
print(j.get_species())


print(Human.grunt())
print(i.grunt())
print(i.age)
i.age = 44
print(i.age)
del i.age
#print(i.age)
