class Bank:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self,money_add):
        money_input = float(input('Введите сумму которую хотите добавить'))
        # self.money_add = money_add
        self._balance = self._balance + money_input
        return self._balance

    def _kill(self):
        if self == 'обнулить':
            self._balance = 0
            return self._balance

    def __jackpot(self):
        self._balance = self._balance * 10
        return self._balance

    def summarize(self):
        self.summarize_amount = self._balance + object
        return self.summarize_amount




# first_client = Bank('Dair', 1000 )
# print(first_client.moneyX(1))

