 class Validator:
    @staticmethod
    def raise_if_str_is_empty_or_whitespace(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_zoro_or_negative(number, message):
        if number <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_not_in_range(number, min_value, max_value, message):
        if number < min_value or number > max_value:
            raise ValueError(message)