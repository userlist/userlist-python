class Resource:
    endpoint = None

    def __init__(self, data):
        if data is None:
            raise ValueError("data parameter is required")
        self.data = data

    def to_dict(self):
        return self.data

    def __getattr__(self, item):
        if item in self.data:
            return self.data[item]

        return super().__getattr__(item)
