# code Open for extension - We should be able to extend functionality the existing code.
# code closed for modification - We should not modify the content of the code.

# Say for the code what we are having in single_responsible.py if we have to add a payment method we need to modify the
# Payment Processor class by adding one more function. Which is modification.

# So we need to define the structure of class and subclass which will handle the situation without updating the original class.


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
    def pay(self, order, security_code):
        pass

class DebitPayment(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing Debit payment mode")
        print("Verifying security code", security_code)
        order.status = "paid"

class CreditPayment(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing Credit payment mode")
        print("Verifying security code", security_code)
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 500)
order.add_item("USB Cable", 10, 25)

# print(order.total_price())
# pay = PaymentProcessor()
cpay = CreditPayment()
cpay.pay(order, 199)

# Now if a new payment come we do not need to modify any class. It can be done as follows

class PayPalPayment(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing PayPal payment mode")
        print("Verifying security code", security_code)
        order.status = "paid"



