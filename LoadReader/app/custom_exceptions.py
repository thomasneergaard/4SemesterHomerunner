class invalid_number_big(Exception):
    'Number is too big'
    pass

class number_deviation_high(Exception):
    """Exception raised for numbers that deviate too much from the average."""
    def __init__(self, number, avg, message="Vaegten har opfanget en for tung vaegt"):
        self.number = number
        self.avg = avg
        self.message = message
        super().__init__(self.message)

class number_deviation_low(Exception):
    """Exception raised for numbers that deviate too much from the average."""
    def __init__(self, number, avg, message="Vaegten har opfanget en for let vaegt"):
        self.number = number
        self.avg = avg
        self.message = message
        super().__init__(self.message)

class weight_too_heavy(Exception):
    """Exception raised for numbers hat go over max_weight"""
    def __init__(self, number, avg, message="Vaegten er for tung"):
        self.number = number
        self.avg = avg
        self.message = message
        super().__init__(self.message)