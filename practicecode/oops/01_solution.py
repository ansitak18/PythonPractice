class Car:
    def __init__(self, brand, model): #self works as this works in js
        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corolla") #object created
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)

#__init__() is a constructor
# and if we dont write self keyword then classes and objects wont be able to access each other