
#self similar to 'this' keyword in java

class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_age(self):
        return self.age
        
    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age
        
    def set_name(self,name):
        self.name = name

#

d = Dog("Tim", 6)
d.set_age(10)

print(d.get_name())
print(d.get_age())



