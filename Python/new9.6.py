# from abc import ABC, abstractmethod

# class UIControl(ABC):
#   @abstractmethod
#   def draw(self):
#     pass
  
# class TextBox(UIControl):
#   def draw(self):
#     print(TextBox)
    
# class DropDownList(UIControl):
#   def draw(self):
#     print(DropDownList)
  
# def draw(controls):
#   for control in controls:
#     control.draw()
    
  
# ddl = DropDownList()
# tbox = TextBox()
# draw([tbox, ddl])


from abc import ABC, abstractmethod

class TextBox:
  def draw(self):
    print(TextBox)
    
class DropDownList:
  def draw(self):
    print(DropDownList)
  
def draw(controls):
  for control in controls:
    control.draw()
    
  
ddl = DropDownList()
tbox = TextBox()
draw([tbox, ddl])