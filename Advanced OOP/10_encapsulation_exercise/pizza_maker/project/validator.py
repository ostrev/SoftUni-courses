class Validator:
    @staticmethod
    def raise_if_string_is_empty(string, message):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_is_zero_or_less(value: float, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_is_none(prop, message):
        if prop is None:
            raise ValueError(message)

