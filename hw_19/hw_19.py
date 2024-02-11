from datetime import datetime

class Car:
    number_of_cars = 0
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance


    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

        Car.number_of_cars += 1


    def car_info(self):
        return f"Brand: {self.__brand}, Model: {self.__model}, Year: {self.__year}"


    def age_of_car(self):
        return f"Car age: {datetime.now().year - self.__year} years."


    @classmethod
    def total_cars(cls):
        return cls.number_of_cars
    
    @property
    def brand(self):
        return self.__brand


    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self.__brand = value
        else:
            raise ValueError("Please input correct value")
        

    @property
    def model(self):
        return self.__model
    

    @model.setter
    def model(self, value):
        if isinstance(value, str):
            self.__model = value
        else:
            raise ValueError("Please input correct value")


    @property
    def year(self):
        return self.__year


    @year.setter
    def year(self, value):
        if isinstance(value, int) and 2000 <= value <= datetime.now().year:
            self.__year = value
        else:
            raise ValueError("Enter right year")        


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)

        self.__battery_life = battery_life


    def battery_info(self):
        return f"The battery life of this car is {self.__battery_life} hours."
    

    @property
    def battery_life(self):
        return self.__battery_life
    

    @battery_life.setter
    def battery_life(self, value):
        if isinstance(value, int) and value > 0:
            self.__battery_life = value
        else:
            raise ValueError("Not integer, negative value or zero not allowed")



#======================

car1 = Car("Mazda", "Verisa", 2005)
el_car_1 = ElectricCar("Tesla", "Model S", 2023, 425)

car1.brand = 'Honda'
el_car_1.brand = 'Shevrolet'

car1.model = 'Civic'
el_car_1.model = 'Volt'

car1.year = 2023
el_car_1.year = 2022

el_car_1.battery_life = 7800

print(car1.car_info())
print(el_car_1.car_info())
print( el_car_1.battery_info())
print(Car.total_cars())

