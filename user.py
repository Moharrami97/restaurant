class Supervisor:
    user_list = list()

    def __init__(self, username, password, full_number, *args, **kwargs):
        self.username = username
        self.password = password
        self.full_number = full_number
        Supervisor.user_list.append(self)
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, username="Narges", password="123", full_number="09101234567"):
        return cls(username, password, full_number)
