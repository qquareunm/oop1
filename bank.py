class Bank:
    def __init__(self, name, head_name, coef):
        self.name = name
        self.head_name = head_name
        self.__coef = coef
        
    @property
    def coef(self):
        return self.__coef
    
    @coef.setter
    def coef(self, value):
        if value >= 0 and value <= 100:
            self.__coef = value
            
    def calculate(self, client, n):
        if n <= 0:
            return
        x = client.money * (1 + self.coef/100)**n
        return x

class Client:
    def __init__(self, name, id, bank, money):
        self.name = name
        self.id = id
        self.bank = bank
        self.__money = money
        self.__money_after_year = None
        
    @property
    def money(self):
        return self.__money
    
    @property
    def money_after_year(self):
        if self.__money_after_year is None:
            self.__money_after_year = self.bank.calculate(self, 1)
        return self.__money_after_year
    
    def invest(self, amount):
        if amount < 0:
            print("Нельзя вводить отрицательное число.")
            return
        self.__money += amount
        
    def take_money(self, amount):
        if amount < 0:
            print("Нельзя вводить отрицательное число.")
            return
        if self.__money - amount < 0:
            print("Нельзя снять больше, чем есть на счету.")
            return
        self.__money -= amount

bank = Bank("Kaspi", "Ps", 0.5) 
client = Client("B.D", "777", bank, 70000) 
print(client.money) 