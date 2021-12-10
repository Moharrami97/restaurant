from datetime import datetime
from uuid import uuid4


class Item:
    food_list = list()
    beverage_list = list()
    starter_list = list()

    def __init__(self, name, price, item_type, *args, **kwargs):
        # item_type: {food, beverage, starter}
        self.uuid = uuid4()
        self.name = name
        self.price = price
        self.item_type = item_type
        self.datetime = datetime.now()
        if self.item_type == "f":
            Item.food_list.append(self)
        elif self.item_type == "b":
            Item.beverage_list.append(self)
        elif self.item_type == "s":
            Item.starter_list.append(self)
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, name="pizza", price=20000, item_type="f"):
        return cls(name, price, item_type)

