from uuid import uuid4


class Table:
    table_list = list()

    def __init__(self, number, capacity, reserved=False, *args, **kwargs):
        self.uuid = uuid4()
        self.number = number
        self.capacity = capacity
        self.reserved = reserved
        self.is_available = True
        Table.table_list.append(self)
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, number=2, reserved=True, capacity=4):
        return cls(number, reserved, capacity)
