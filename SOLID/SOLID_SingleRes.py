class Order:
    item =[]
    quantities =[]
    price =[]
    status ="open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):
        total = 0;
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total



class PaymentProcessor:

    def pay_credit (self, order, security_code):
            print("processing credit payment")
            print(f"verifying security code: {security_code}")
            order.status = "paid"
    def pay_debit (self, order, security_code):
            print("processing credit payment")
            print(f"verifying security code: {security_code}")
            order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order, "123495")








