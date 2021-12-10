class Order:
    def __init__(self, bill, table, item_dict=None, in_out=False, *args, **kwargs):
        self.uuid = uuid4()
        self.bill = bill
        self.table = table
        self.item_dict = item_dict
        self.in_out = in_out
        self.datetime = datetime.now()
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, bill=Bill.sample(), table=Table.sample, item_dict=2, in_out=True):
        return cls(bill, table, item_dict, in_out)
