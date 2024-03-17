from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address


class Customer(User):
    def __init__(self, name, phone, address, money):
        super.__init__(name, phone, address)
        self.wallet = money
