class Relation:
    def __init__(self, client, resource_class):
        self.client = client
        self.resource_class = resource_class

    def push(self, data):
        resource = self.resource_class(data)
        self.client.post(self.resource_class.endpoint, resource.to_dict())

    def create(self, data):
        return self.push(data)

    def update(self, data):
        return self.push(data)

    def delete(self, data):
        resource = self.resource_class(data)
        self.client.delete(self.resource_class.endpoint, resource.to_dict())
