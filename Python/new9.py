class Product:
  
  # def __init__(self, price):
  #   self.set_price(price)
    
  # def get_price(self):
  #   return self.__price
  
  # def set_price(self, value):
  #   if value < 0:
  #     raise ValueError("Price cannot be negative.")
  #   self.__price = value
    
    
  def __init__(self, price):
    self.price = price
    
  @property
  def price(self):
    return self.__price
  
  @price.setter
  def price(self, value):
    if value < 0:
      raise ValueError("Price cannot be negative.")
    self.__price = value
    

product = Product(5)
print(product.price)