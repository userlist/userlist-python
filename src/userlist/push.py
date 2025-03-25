from .client import Client
from .config import Config
from .relation import Relation
from .resources.company import Company
from .resources.user import User
from .resources.event import Event
from .resources.relationship import Relationship
from .resources.message import Message


class Push:
    def __init__(self, **config):
        self.config = Config(**config)
        self.client = Client(self.config)

        # Initialize relations for each resource
        self.users = Relation(self.client, User)
        self.companies = Relation(self.client, Company)
        self.events = Relation(self.client, Event)
        self.relationships = Relation(self.client, Relationship)
        self.messages = Relation(self.client, Message)
