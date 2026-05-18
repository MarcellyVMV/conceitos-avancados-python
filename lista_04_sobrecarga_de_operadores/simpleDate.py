class SimpleDate:
    #Construtor
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    #Método para imprimir a data
    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"

    #Método para comparar se as datas são iguais
    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    #Método para comparar se as datas são diferentes
    def __ne__(self, other):
        return not self == other

    #Método para comparar se a data é menor que outra
    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else:
                return self.day < other.day

    #Método para comparar se a data é maior que outra
    def __gt__(self, other):
        return not self < other

    #Método para somar uma quantidade de dias a data
    def __add__(self, days):
        new_day = self.day + days
        new_month = self.month
        new_year = self.year

        while new_day > 30:
            new_day -= 30
            new_month += 1
            while new_month > 12:
                new_month = 1
                new_year += 1

        return SimpleDate(new_day, new_month, new_year)

    #Método para subtrair duas datas
    def __sub__(self, other):
        days = (360 * (self.year - other.year)) + (30 * (self.month - other.month)) + (self.day - other.day)
        return abs(days)

#Exemplo
d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(28, 12, 1985)
d3 = SimpleDate(28, 12, 1985)

print(f"\nd1 é: {d1}") #Output: 04/10/2020
print(f"d2 é: {d2}") #Output: 28/12/1985
print(f"d3 é: {d3}") #Output: 28/12/1985

print(f"\nd1 e d2 são Iguais? {'Sim' if d1 == d2 else 'Não'}") #Output: Não
print(f"d1 e d2 são Diferentes? {'Sim' if d1 != d2 else 'Não'}") #Output: Sim
print(f"d1 e d3 são Iguais? {'Sim' if d1 == d3 else 'Não'}") #Output: Não
print(f"d1 é menor que d2? {'Sim' if d1 < d2 else 'Não'}") #Output: Não
print(f"d1 é maior que d2? {'Sim' if d1 > d2 else 'Não'}") #Output: Sim

d4 = d1 + 3
d5 = d2 + 400

print(f"\nd1 + 3 dias é a data(d4): {d4}") #Output: 07/10/2020
print(f"d2 + 400 dias é a data(d5): {d5}") #Output: 08/02/1987

d6 = SimpleDate(2, 11, 2020)
print(f"d6 é: {d6}") #Output: 02/11/2020

print(f"\nA diferença entre d1 e d6 é de {d1-d6} dias") #Output: -28
print(f"A diferença entre d6 e d1 é de {d6-d1} dias") #Output: 28
print(f"A diferença entre d1 e d3 é de {d1-d3} dias\n") #Output: 12516