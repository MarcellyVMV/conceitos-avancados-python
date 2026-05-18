class Animal:
    #Função inicial
    def __init__(self, name, species, position):
        self.name = name
        self.species = species
        self.position = position

class Position:
    #Função inicial
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Forest:
    #Função inicial
    def __init__(self):
        self.animals = []

    #Função para adicionar animais da lista
    def add_animal(self, animal):
        self.animals.append(animal)

    #Função para remover animais da lista
    def remove_animal(self, animal):
        self.animals.remove(animal)

    #Função para imprimir o total de animais
    def print_total_animals(self):
        print(f"\nHá {len(self.animals)} animais na floresta.\n")

    #Função para mover todos os animais
    def move_all_animals(self, dx, dy):
        for animal in self.animals:
            new_position = Position(animal.position.x + dx, animal.position.y + dy)
            animal.position = new_position

# Exemplo
forest = Forest()

animal1 = Animal("Aslan", "Leão", Position(10, 10))
animal2 = Animal("Puff", "Urso", Position(20, 20))

forest.add_animal(animal1)
forest.add_animal(animal2)

forest.print_total_animals()

forest.move_all_animals(5, 5)

animal1.position.x = 150
animal1.position.y = 150

print(f"{animal1.name} foi movido para a posição ({animal1.position.x}, {animal1.position.y}).\n")