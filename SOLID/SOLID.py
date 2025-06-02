# SOLID
# S - Single Responsibility
# O - Open Close
# L - Liskov Substitution
# I - Interface Segregation
# D - Dependency Inversion

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

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing Debit payment mode")
            print("Verifying security code", security_code)
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing Credit payment mode")
            print("Verifying security code", security_code)
            self.status = "paid"
        else:
            raise Exception(f"Unknown Payment method: {payment_type}")

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 500)
order.add_item("USB Cable", 10, 25)

print(order.total_price())
order.pay("credit", 199)


