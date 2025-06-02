# Classes and methods should have single responsibility. Not too many functionalities should be handled.

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

class PaymentProcessor:
    def debit_pay(self, order, security_code):
        print("Processing Debit payment mode")
        print("Verifying security code", security_code)
        order.status = "paid"

    def credit_pay(self, order, security_code):
        print("Processing Credit payment mode")
        print("Verifying security code", security_code)
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 500)
order.add_item("USB Cable", 10, 25)

# print(order.total_price())
pay = PaymentProcessor()
pay.credit_pay(order, 199)


