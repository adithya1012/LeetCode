# Liscov tells that: class B extends class A then if there is a situation we need to replace class B
# with class A it should not break. So it will happen if we narrow down the ability of parent class.

# example 1:
class Bike:
    def turnOnEngine(self):
        pass
    def accelerate(self):
        pass

class Motorcycle(Bike):
    def __init__(self):
        self.start = "off"
        self.speed = 0

    def turnOnEngine(self):
        self.start = "on"

    def accelerate(self):
        self.speed += 10

class Bicycle(Bike):
    def __init__(self):
        self.speed = 0
    def turnOnEngine(self):
        raise "Bicycle cannot be turned on"
    def accelerate(self):
        self.speed += 10

b = Bicycle()
try:
    b.turnOnEngine() # THIS is not correct. Now we are reducing the capability of Bike parent class. It should be in
# increasing order. The number arguments or methods keep on increasing down the hierarchy.
except:
    pass
# Example 2:
# In the previous order example, PayPal will not take any security code. Instead it will take the email id. In that case
# if we just replace the security_code with email id it is not making sense. Hence we need to update in the parent level.not

from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i]*self.prices[i]
        return total

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass

class DebitPayment(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing Debit payment mode")
        print("Verifying security code", self.security_code)
        order.status = "paid"

class CreditPayment(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order):
        print("Processing Credit payment mode")
        print("Verifying security code", self.security_code)
        order.status = "paid"

class PayPalPayment(PaymentProcessor):
    def __init__(self, email):
        self.email = email # this is the differnt element not present in other payments.

    def pay(self, order):
        print("Processing PayPal payment mode")
        print("Verifying security code", self.email)
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 500)
order.add_item("USB Cable", 10, 25)

# print(order.total_price())
# pay = PaymentProcessor()
cpay = CreditPayment(199)
cpay.pay(order)





