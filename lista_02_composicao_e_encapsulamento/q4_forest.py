class Forest:
    #Função inicial
    def __init__(self, width, height):
        self.animals = []
        self.width = width
        self.height = height

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
    def move_all_animals(self, dx, dy, forest):
        for animal in self.animals:
            new_position = Position(animal.position.x + dx, animal.position.y + dy, forest)
            animal.position = new_position

class Animal:
    #Função inicial
    def __init__(self, name, species, position):
        self.name = name
        self.species = species
        self.position = position

class Position:
    #Função inicial
    def __init__(self, x, y, forest):
        self._x = x
        self._y = y
        self.forest = forest

    #Getters e Setters
    @property
    #Retorna a coordenada x
    def x(self):
        return self._x

    @x.setter
    #Define a coordenada x
    def x(self, newx):
        if newx >= 0 and newx <= forest.width:
            self._x = newx
        else:
            raise ValueError(f"A coordenada x não pode ser menor a zero nem maior que {forest.width}")

    @property
    #Retorna a coordenada y
    def y(self):
        return self._y

    @y.setter
    #Define a coordenada y
    def y(self, newy):
        if newy >= 0 and newy <= forest.height:
            self._y = newy
        else:
            raise ValueError(f"A coordenada y não pode ser menor a zero nem maior que {forest.height}")

#Exemplo
forest = Forest(100, 100)

animal1 = Animal("Aslan", "Leão", Position(10, 10, forest))
animal2 = Animal("Puff", "Urso", Position(20, 20, forest))

forest.add_animal(animal1)
forest.add_animal(animal2)

forest.print_total_animals()

forest.move_all_animals(5, 5, forest)

animal1.position.x = 50
animal1.position.y = 50

print(f"{animal1.name} foi movido para a posição ({animal1.position.x}, {animal1.position.y}).\n")