class Car:
    def __init__(self, brand, model): #self works as this works in js
        self.brand = brand
        self.model = model
#2nd question 
    def full_name(self):
        return f"{self.brand} {self.model}"
    
#inheritance 3rd question
class ElectricCar(Car): 
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model) #inheriting elements from the above class Car using super keyword 
        self.battery_size = battery_size
# 3rd question 
my_tesla = ElectricCar("Tesla", "Model S", "85kWH")
print(my_tesla.model)
print(my_tesla.full_name())#it can also access full_name which is in the Car class but inside different function 

my_car = Car("Toyota", "Corolla") #object created
print(my_car.brand)
print(my_car.model)
print(my_car.full_name()) #2nd question

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)

#__init__() is a constructor
# and if we dont write self keyword then classes and objects wont be able to access each other
#so self acts like a connection between class and objects