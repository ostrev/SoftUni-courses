from project.dough import Dough
from project.topping import Topping
from project.validator import Validator


class Pizza:
    def __init__(self, name: str, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty(value, 'The name cannot be an empty string')
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        Validator.raise_if_is_none(value, 'You should add dough to the pizza')
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        Validator.raise_if_is_zero_or_less(value, "The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

        # for k, v in self.toppings.items():
        #     if k == topping.topping_type:
        #         self.toppings[topping.topping_type] += topping.weight
        #     return
        # self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_dough = self.dough.weight + sum(self.toppings.values())
        return total_dough
