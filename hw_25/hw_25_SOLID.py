# TODO SOLID პრინციპის დაცვით შეცვალეთ კლასების იმპლემენტაცია

# Single Responsibility Principle
class Book:
    def set_details(self, title, author):
        pass
    def get_discount_price(self, discount):
        pass
#================================================
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class DiscountCalculator:
    def get_discount_price(self, price, discount):
        return price * (1 - discount)



# TODO დაამატეთ  PayPal-ის გადახდების კლასი, და  Payment
# Open/Closed Principle
class Payment:
    """  გადახდის კლასი საკრედიტო ბარათით გადახდების დასამუშავებლად
    """
    def process_credit(self, amount):
        pass

class PayPalPayment(Payment):
    """  გადახდის კლასი PayPal გადახდების დასამუშავებლად
    """
    def process_paypal(self, amount):
        pass


# TODO გადააკეთეთ კლასები ისე, რომ დაიცვან ლისკოვის ჩანაცვლების პრინციპი
# Liskov Substitution Principle
class Vehicle:
    def fuel_capacity(self):
        return "100 liters"

class ElectricCar(Vehicle):
    def __init__(self):
        self.battery_capacity = "Battery capacity is 100 kWh"

    def fuel_capacity(self):
        return self.battery_capacity



# TODO შეცვალეთ იმპლემენტაცია, რადგან ყველა მოთამაშეს არ აქვს აუდიოს ან ვიდეოს მხარდაჭერა
# Interface Segregation Principle
class MultimediaPlayer:
    def play_audio(self):
        pass
    def play_video(self):
        pass

#===================================
class AudioPlayer:
    def play_audio(self):
        pass

class VideoPlayer:
    def play_video(self):
        pass



# TODO შეცვალეთ კლასის იმპლემენტაცია, რომ დაიცვას დამოკიდებულების ინვერსიის პრინციპი.
# Dependency Inversion Principle (DIP)
class DisplayInterface:
    def show(self, data):
        pass

class ConsoleDisplay:
    def show(self, data):
        print(data)

class WeatherStation:
    def report(self, display):
        display.show("Weather Data")
#========================
console_display = ConsoleDisplay()
weather_station = WeatherStation()
weather_station.report(console_display)