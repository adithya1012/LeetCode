# This principle tess that Interfaces such that the client/child classes should not implement unnecessary
# functions they do not need.

# Say in the previous example we have 2 factor acuthentication present as part of payment processing as abstract
# classes. So all the child classes are compelled to implement the 2 factor auth. But credict card do not require any
# 2 factor acuth. So it will define it and infunction body it may throw error or leave withput doing any operation.
# this is a bad approch and this needs to be handles through creating the subclasses in the interface level so that
# correct abstract class will be extended.


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

    # MOVED TO DIFFERENT CLASS
    # @abstractmethod
    # def twoFactorAuth(self):
    #     pass

class PaymentAuthentication(PaymentProcessor):
    @abstractmethod
    def twoFactorAuth(self):
        pass

class DebitPayment(PaymentAuthentication):
    def __init__(self, security_code):
        self.security_code = security_code
        self.auth = False

    def pay(self, order):
        if self.auth:
            print("Processing Debit payment mode")
            print("Verifying security code", self.security_code)
            order.status = "paid"
        else:
            print("Authentication Failed")

    def twoFactorAuth(self):
        self.auth = True


class CreditPayment(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order):
        print("Processing Credit payment mode")
        print("Verifying security code", self.security_code)
        order.status = "paid"

    # NOT NECESSARY
    # def twoFactorAuth(self):
    #     raise "There won't be any 2 factor auth for credit cared"

class PayPalPayment(PaymentAuthentication):
    def __init__(self, email):
        self.email = email
        self.auth = False

    def pay(self, order):
        if self.auth:
            print("Processing PayPal payment mode")
            print("Verifying security code", self.email)
            order.status = "paid"
        else:
            print("Authentication Failed")

    def twoFactorAuth(self):
        self.auth = True

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 500)
order.add_item("USB Cable", 10, 25)

# print(order.total_price())
# pay = PaymentProcessor()
ppay = PayPalPayment("email@gmail.com")
ppay.pay(order) # Auth Failed
ppay.twoFactorAuth()
ppay.pay(order)





