"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        "establishes start and current value"

        self.start = start
        self.current = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.current}>"

    def generate(self):
        "returns current and increments current"
        result = self.current
        self.current += 1
        return result

    def reset(self):
        "puts the current back at the start"
        self.current = self.start