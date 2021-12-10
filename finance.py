from datetime import datetime
from uuid import uuid4


class Bill:
    def __init__(self, total_price, payment, *args, **kwargs):
        self.uuid = uuid4()
        self.total_price = total_price
        self.payment = payment
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, total_price=100000):
        return cls(total_price, payment=Payment.sample())


class Payment:
    def __init__(self, payment_type, price, *args, **kwargs):
        self.uuid = uuid4()
        self.payment_type = payment_type
        self.price = price
        self.is_paid = False
        self.datetime = datetime.now()
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, payment_type="online", price=100000,):
        return cls(payment_type, price)

