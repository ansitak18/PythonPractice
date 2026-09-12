class Car:

    #total cars created - classes and variables
    total_cars = 0


    def __init__(self, brand, model): #self works as this works in js
        self.__brand = brand
        self.model = model
        Car.total_cars += 1 # or self.total_car



    # 4th question about encapsualtion making private variable by adding two underscore __attributename
    def get_brand(self):
        return self.__brand + "!" # can add more characters by simply using + 
    
#2nd question 
    def full_name(self):
        return f"{self.__brand} {self.model}"

#for polymorphism
    def fuel_type(self):
        return 'Petrol or Diesel'
    
#inheritance 3rd question
class ElectricCar(Car): 
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model) #inheriting elements from the above class Car using super keyword 
        self.battery_size = battery_size

    def fuel_type(self):
        return 'Electric charge'
# 3rd question 
my_tesla = ElectricCar("Tesla", "Model S", "85kWH")
print(my_tesla.model)
print(my_tesla.full_name())#it can also access full_name which is in the Car class but inside different function 
print(my_tesla.fuel_type()) #polymorphism

Car("Tata", "Safari") #object creation
#print(safari.total_cars) # dont access the numbers like this as it may give the wrong result 
print(Car.total_cars) #correct way 

my_car = Car("Toyota", "Corolla") #object created without holding any reference for the object created
#print(my_car.brand) #does not give direct access because brand attribute is now private
print(my_car.model)
print(my_car.full_name()) #2nd question
print(my_car.fuel_type()) #polymorphism
my_new_car = Car("Tata", "Safari")
print(my_new_car.model)

#accessing private attributes - encapsulation
#print(my_car.__brand) #does not give direct access as it is declared as private in above code
print(my_car.get_brand()) #using parentheses because we are calling a function method

#__init__() is a constructor
# and if we dont write self keyword then classes and objects wont be able to access each other
#so self acts like a connection between class and objects