class ShippingContainer:
    next_serial = 13364

    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):  # class level attributes
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial  # observe how static method return value
        ShippingContainer.next_serial += 1  # this is how to access a class level attribute

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result