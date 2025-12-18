# polymorphism
class PaymentSystem:
    def pay():
        pass

class CreditCardPayment(PaymentSystem):
    def pay(self):
        print("Processing credit card payment...")

class UpiPayment(PaymentSystem):
    def pay(self):
        print("Processing UPI payment...")

class CashPayment(PaymentSystem):
    def pay(self):
        print("Processing cash payment...")

cash = [CreditCardPayment(), UpiPayment(), CashPayment()]

for p in cash:
    p.pay()