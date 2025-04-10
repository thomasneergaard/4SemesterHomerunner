class invalid_number_big(Exception):
    'Number is too big'
    pass

class number_deviation_high(Exception):
    """Exception raised for numbers that deviate too much from the average."""
    def __init__(self, number, avg, message="Vægten har opfanget en for tung vægt"):
        self.number = number
        self.avg = avg
        self.message = message
        super().__init__(self.message)

class number_deviation_low(Exception):
    """Exception raised for numbers that deviate too much from the average."""
    def __init__(self, number, avg, message="Vægten har opfanget en for let vægt"):
        self.number = number
        self.avg = avg
        self.message = message
        super().__init__(self.message)

class weight_too_heavy(Exception):
    """Exception raised for numbers that go over max_weight"""
    def __init__(self, avg, message="Vægten er for tung"):
        self.avg = avg
        self.message = message
        super().__init__(self.message)