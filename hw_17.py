from datetime import date

class Car:
    number_of_cars = 0
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        Car.number_of_cars += 1


    def car_info(self):
       print(f"Brand: {self.__brand}, Model: {self.__model}, Year: {self.__year}")


    def age_of_car(self):
        today = date.today().year
        car_age = today - int(self.__year)
        return car_age


    def total_cars(self):
        print(f"{Car.number_of_cars}")
        # return Car.number_of_cars()


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.__battery_life = battery_life
        
    
    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.__battery_life} საათი")
    
        
#===================================
car1 = Car('Kia', 'Optima', '2018')
car1.car_info()
print(f"Car {car1._Car__brand} is {car1.age_of_car()} years")

car2 = ElectricCar('Toyota', 'Prius', '2013', '2500')
car2.car_info()
car2.battery_info()

# print(Car.total_cars())
# total_cars()
# Car.total_cars()
print(Car.number_of_cars)
print(Car.total_cars)