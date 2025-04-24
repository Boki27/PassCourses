class Animal:
  def eat(self):
    print("eat")

#Animal: Parent, Base
#Bird: Child, Sub
class Bird(Animal):   
  def fly(self):
    print("fly")
    
class Chicken(Bird):
  pass
