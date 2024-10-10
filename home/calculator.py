class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def add(self):
        return self.first_number + self.second_number

    def sub(self):
        return self.first_number - self.second_number

    def mul(self):
        return self.first_number * self.second_number

    def truediv(self):
        return self.first_number // self.second_number

x = Calculator(20, 12)
print(x.add())
print(x.sub())
print(x.mul())
print(x.truediv())