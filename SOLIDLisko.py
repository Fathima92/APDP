from abc import ABC, abstractmethod

class Order:
    item = []
    quantities = []
    price = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):

        total = 0
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order):
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order):
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address):
        self.email_address = email_address
    def pay(self, order):
        print("processing credit payment")
        print(f"verifying security code: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("abc@gmail.com")
pro2 =CreditPaymentProcessor(123456)
pro3 = DebitPaymentProcessor(456895)
processor.pay(order)








