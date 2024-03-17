from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address, money):
        super.__init__(name, phone, email, address)
        self.wallet = money
        self.__order = order

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        print(f'{self.name} placed an order {order.items}')

    def eat_food(self, order):
        pass

    def pay_for_order(self, amount):
        pass

    def give_tips(self, tips_amount):
        pass

    def write_review(self, stars):
        pass


class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_date, department):
        super.__init__(name, phone, email, address)
        self.salary = salary
        self.starting_date = starting_date
        self.department = department


class Chep(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department, cooking_item):
        super.__init__(name, phone, email, address,
                       salary, starting_date, department)
        self.cooking_item = cooking_item


class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department):
        super.__init__(name, phone, email, address,
                       salary, starting_date, department)


class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department):
        super.__init__(name, phone, email, address,
                       salary, starting_date, department)
