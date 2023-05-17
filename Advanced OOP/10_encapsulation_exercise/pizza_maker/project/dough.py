from project.validator import Validator


class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight



    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, value):
        Validator.raise_if_string_is_empty(value, 'The flour type cannot be an empty string')
        self.__flour_type = value

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, value):
        Validator.raise_if_string_is_empty(value, 'The baking technique cannot be an empty string')
        self.__baking_technique = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        Validator.raise_if_is_zero_or_less(value, 'The weight cannot be less or equal to zero')
        self.__weight = value

