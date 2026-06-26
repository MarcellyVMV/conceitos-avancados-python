from __future__ import annotations


# 3. Crie um programa em que os animais se movimentam em uma determinada área de floresta. Crie uma classe Animal, que tenha como atributos name e species.
class Animal:
    """
    Representa um animal em uma floresta.

    Attributes:
        name (str): Nome do animal.
        species (str): Espécie do animal.
        position (Position): Posição do animal na floresta.
    """

    def __init__(self, name: str, species: str, position: Position) -> None:
        """
        Inicializa um animal com suas características principais.

        Args:
            name (str): Nome do animal.
            species (str): Espécie do animal.
            position (Position): Posição do animal na floresta.
        """
        if not isinstance(position, Position):
            raise TypeError("A posição do animal deve ser da classe 'Position'.")
        self.name = name
        self.species = species
        self.position = position

    def __str__(self) -> str:
        """
        Representa o animal como uma string.

        Returns:
            str: Uma string formatada com as informações do animal.
        """
        return (
            f"Nome: {self.name}\n"
            f"Espécie: {self.species}\n"
            f"Posição: ({self.position.x}, {self.position.y})\n"
        )

    def move(self, dx: float = 0, dy: float = 0) -> None:
        """
        Move o animal para uma nova posição.

        Args:
            dx (float): A distância a ser movida no eixo x.
            dy (float): A distância a ser movida no eixo y.
        """
        self.position.x += dx
        self.position.y += dy


class Forest:
    """
    Representa uma floresta.

    Attributes:
        width (float): Largura da floresta.
        height (float): Altura da floresta.
        animals (list): Lista dos animais na floresta.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Inicializa a floresta com largura, altura e uma lista de animais.

        Args:
            width (float): Largura da floresta.
            height (float): Altura da floresta.
        """
        self.width = abs(width)
        self.height = abs(height)
        # 3.1  Manter o controle de todos os animais presentes.
        self.animals: list[Animal] = []

    def __str__(self) -> str:
        """
        Representa a floresta como uma string.

        Returns:
            str: Uma string formatada com as informações da floresta e seus animais.
        """
        return (
            f"Floresta: {self.width} x {self.height}\n"
            f"Total de animais: {len(self.animals)}\n"
            f"Animais na floresta:\n{"\n\n".join(str(animal) for animal in self.animals)}\n"
        )

    # 3.2  Ter um método para adicionar um novo animal.
    def add_animal(self, animal: Animal) -> None:
        """
        Adiciona um animal à lista de animais na floresta.

        Args:
            animal (Animal): Animal a ser adicionado à floresta.
        """
        if not isinstance(animal, Animal):
            raise TypeError(
                "O animal adicionado deve ser um objeto da classe 'Animal'."
            )
        self.animals.append(animal)

    # 3.3  Ter um método para remover um animal.
    def remove_animal(self, animal: Animal) -> bool:
        """
        Remove um animal da lista de animais na floresta.

        Args:
            animal (Animal): Animal a ser removido da floresta.

        Returns:
            bool: True se o animal foi removido com sucesso, False se o animal não foi encontrado na floresta.
        """
        if animal not in self.animals:
            return False
        self.animals.remove(animal)
        return True

    # 3.4  Ter um método que imprime o número total de animais ativos na floresta.
    def total_animals(self) -> int:
        """
        Retorna o total de animais na floresta.

        Returns:
            int: O número total de animais na floresta.
        """
        return len(self.animals)

    # 3.5  Ter um método que permite que todos os animais se movam simultaneamente, por valores específicos de coordenadas x e y
    def move_all_animals(self, dx: float = 0, dy: float = 0) -> None:
        """
        Move simultaneamente todos os animais da floresta.

        Args:
            dx (float): Deslocamento aplicado no eixo x.
            dy (float): Deslocamento aplicado no eixo y.
        """
        for animal in self.animals:
            animal.move(dx, dy)


class Position:
    """
    Representa a posição de um animal em uma floresta.

    Attributes:
        forest (Forest): Floresta onde o animal está localizado.
        x (float): Coordenada x.
        y (float): Coordenada y.
    """

    def __init__(self, forest: Forest, x: float, y: float) -> None:
        """
        Inicializa a posição com coordenadas x e y, e referência à floresta.

        Args:
            forest (Forest): Floresta onde o animal está localizado.
            x (float): Coordenada x.
            y (float): Coordenada y.
        """
        self.forest = forest
        self.x = x
        self.y = y

    # --- Getters e Setters --- #
    @property
    def x(self) -> float:
        """
        Retorna a coordenada x do animal.

        Returns:
            float: A coordenada x do animal.
        """
        return self._x

    @x.setter
    def x(self, newx: float) -> None:
        """
        Define a coordenada x do animal, garantindo que esteja dentro dos limites da floresta.

        Args:
            newx (float): A nova coordenada x do animal.
        """
        if newx >= 0 and newx <= self.forest.width:
            self._x = newx
        else:
            raise ValueError(
                f"A coordenada x não pode ser menor a zero nem maior que {self.forest.width}"
            )

    @property
    def y(self) -> float:
        """
        Retorna a coordenada y do animal.

        Returns:
            float: A coordenada y do animal.
        """
        return self._y

    @y.setter
    def y(self, newy: float) -> None:
        """
        Define a coordenada y do animal, garantindo que esteja dentro dos limites da floresta.

        Args:
            newy (float): A nova coordenada y do animal.
        """
        if newy >= 0 and newy <= self.forest.height:
            self._y = newy
        else:
            raise ValueError(
                f"A coordenada y não pode ser menor a zero nem maior que {self.forest.height}"
            )


def main():
    # Exemplo
    forest = Forest(100, 100)
    print("\nBem-vindo à floresta Amazônia!\n")

    aslan = Animal("Aslan", "Leão", Position(forest, 10, 10))
    puff = Animal("Puff", "Urso", Position(forest, 20, 20))

    forest.add_animal(aslan)
    forest.add_animal(puff)

    print(f"Total de animais na floresta: {forest.total_animals()}\n")

    forest.move_all_animals(5, 5)

    aslan.move(10, 0)
    print(
        f"{aslan.name} foi movido para a posição ({aslan.position.x}, {aslan.position.y}).\n"
    )

    if forest.remove_animal(puff):
        print(f"{puff.name} foi removido da floresta.\n")
    else:
        print(f"{puff.name} não foi encontrado na floresta.\n")

    print(forest)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
