class Animal:
  
  def __init__(self):
    self.age = 1
    
    print("Animal Constructor")
  
  def eat(self):
    print("eat")

#Animal: Parent, Base
#Mammal: Child, Sub
class Mammal(Animal):  
  
  def __init__(self):
    print("Mammal Constructor")
    self.weight = 2
    super().__init__()
     
  def walk(self):
    print("walk")
    
m = Mammal()
print(m.age)
print(m.weight)
# print(isinstance(m, Animal))
# print(isinstance(m, object))

