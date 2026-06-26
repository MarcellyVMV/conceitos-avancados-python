from math import pi, sqrt


# 5. Crie uma classe Moon que represente uma lua de um Planeta.
class Moon:
    """
    Representa uma lua que orbita um planeta.

    Attributes:
        name (str): Nome da lua.
        diameter (float): Diâmetro da lua em km.
        distance_from_planet (float): Distância da lua ao planeta em km.
    """

    def __init__(self, name: str, diameter: float, distance_from_planet: float) -> None:
        """
        Inicializa uma lua com suas características principais.

        Args:
            name (str): Nome da lua.
            diameter (float): Diâmetro da lua em km.
            distance_from_planet (float): Distância da lua ao planeta em km.
        """
        self.name = name
        self.diameter = abs(diameter)
        self.distance_from_planet = abs(distance_from_planet)

    def __str__(self) -> str:
        """
        Retorna uma representação textual formatada da lua.

        Returns:
            str: String contendo o nome, o diâmetro e a distância da lua ao planeta.
        """
        return (
            f"\tLua: {self.name}\n"
            f"\tDiâmetro: {self.diameter:.2f} km\n"
            f"\tDistância do Planeta: {self.distance_from_planet:.2f} km"
        )


# 1. Crie uma classe chamada Planet que represente um planeta do sistema solar.
class Planet:
    """
    Representa um planeta do sistema solar.

    Attributes:
        name (str): Nome do planeta.
        mass (float): Massa do planeta em kg.
        diameter (float): Diâmetro do planeta em km.
        distance_from_sun (float): Distância do planeta ao Sol em km.
        moons (list[Moon]): Lista de luas que orbitam o planeta.
    """

    # Constantes
    G = 6.674e-11
    SUN_MASS = 1.989e30
    KM_TO_M = 1000
    SECONDS_PER_YEAR = 365.25 * 24 * 3600

    def __init__(
        self, name: str, mass: float, diameter: float, distance_from_sun: float
    ) -> None:
        """
        Inicializa um planeta com suas características principais.

        Args:
            name (str): Nome do planeta.
            mass (float): Massa do planeta em kg.
            diameter (float): Diâmetro do planeta em km.
            distance_from_sun (float): Distância do planeta ao Sol em km.
        """
        self.name = name
        self.mass = abs(mass)
        self.diameter = abs(diameter)
        self.distance_from_sun = abs(distance_from_sun)
        # 5.1 ▪ Adicione um novo atributo à classe Planet denominado moons, que deve ser uma lista de objetos do tipo Moon.
        self.moons: list[Moon] = []

    # 2. Adicione a sua classe do exercício (1), um método describe, que imprima os detalhes do Planeta.
    """def describe(self) -> str:
        return (f"Planeta: {self.name}\nMassa: {self.mass:.2e} kg\nDiâmetro: {self.diameter:.2f} km\n"
            f"Distância do Sol: {self.distance_from_sun:.2f} km\n")"""

    # 3. Substitua o método describe do exercício anterior pelo método especial __str__.
    def __str__(self) -> str:
        """
        Retorna uma representação textual formatada do planeta.

        Returns:
            str: String contendo o nome, a massa, o diâmetro e a distância do planeta ao Sol.
        """
        return (
            f"Planeta: {self.name}\n"
            f"Massa: {self.mass:.2e} kg\n"
            f"Diâmetro: {self.diameter:.2f} km\n"
            f"Distância do Sol: {self.distance_from_sun:.2f} km\n"
            f"Período orbital: {self.orbital_period():.2f} anos\n"
            f"Luas:\n{self.describe_moons()}"
        )

    # 4. Crie um método para calcular e retornar o período orbital do planeta.
    def orbital_period(self) -> float:
        """
        Calcula o período orbital do planeta ao redor do Sol.
        O cálculo é realizado a partir da Terceira Lei de Kepler, considerando a distância média entre o planeta e o Sol.

        Returns:
            float: Período orbital do planeta em anos terrestres.
        """
        # km -> m
        radius_meters = self.distance_from_sun * Planet.KM_TO_M
        # Período em segundos usando a Terceira Lei de Kepler
        period_seconds = (
            2 * pi * sqrt((radius_meters**3) / (Planet.G * Planet.SUN_MASS))
        )
        # s -> anos
        return period_seconds / Planet.SECONDS_PER_YEAR

    # 5.2 ▪ Adicione um método add_moon( self, moon) que receba um objeto Moon como parâmetro e o adicione à lista de luas (moons).
    def add_moon(self, moon: Moon) -> None:
        """
        Adiciona uma lua à lista de luas que orbitam o planeta.

        Args:
            moon (Moon): Objeto representando a lua a ser associada ao planeta.
        """
        if not isinstance(moon, Moon):
            raise TypeError("O argumento moon deve ser um objeto do tipo Moon.")
        self.moons.append(moon)

    # 5.3 ▪ Crie um método describe_moons, que chame o método __str__ de cada uma das suas luas.
    def describe_moons(self) -> str:
        """
        Gera uma descrição textual das luas cadastradas no planeta.
        Caso o planeta não possua luas associadas, retorna uma mensagem informando essa condição.

        Returns:
            str: Descrição formatada contendo os dados de todas as luas cadastradas ou uma mensagem indicando que não há luas registradas.
        """
        if not self.moons:
            return "Nenhuma lua cadastrada."
        return "\n\n".join(str(moon) for moon in self.moons)


# 6. Crie uma classe SolarSystem que represente um sistema solar.
class SolarSystem:
    """
    Representa o sistema solar.

    Attributes:
        planets (list[Planet]): Lista de planetas que compõem o sistema solar.
    """

    def __init__(self) -> None:
        """
        Inicializa um sistema solar com uma lista vazia de planetas.
        """
        self.planets: list[Planet] = []

    # 6.1 ▪ add_planet(self, planet): adicionar um objeto Planet à lista de planetas (planets).
    def add_planet(self, planet: Planet) -> None:
        """
        Adiciona um planeta à lista de planetas que compõem o sistema solar.

        Args:
            planet (Planet): Objeto representando o planeta a ser adicionado ao sistema solar.
        """
        if not isinstance(planet, Planet):
            raise TypeError("O argumento planet deve ser um objeto do tipo Planet.")
        self.planets.append(planet)

    def get_planet(self, name: str) -> Planet | None:
        """
        Procura um planeta pelo nome.

        Args:
            name (str): Nome do planeta.

        Returns:
            Planet | None: O planeta encontrado ou None.
        """
        for planet in self.planets:
            if planet.name.lower() == name.lower():
                return planet
        return None

    # 6.2 ▪ describe(self, name=0): se for fornecido um nome, descreve os detalhes do planeta específico com o nome. Caso contrário, escreve os detalhes de todos os planetas.
    def describe(self, name: str = None) -> str:
        """
        Descreve os detalhes de um planeta específico ou de todos os planetas do sistema solar.

        Se um nome de planeta for fornecido, a função busca e retorna os detalhes do planeta correspondente. Caso contrário, retorna os detalhes de todos os planetas cadastrados no sistema solar.

        Args:
            name (str): Nome do planeta a ser descrito. Se None, serão descritos todos os planetas.

        Returns:
            str: Descrição formatada do planeta específico ou de todos os planetas do sistema solar, ou uma mensagem indicando que nenhum planeta foi encontrado ou cadastrado.
        """
        if not self.planets:
            return "Nenhum planeta cadastrado."
        if name is None:
            return (
                "Planetas cadastrados\n"
                + ("=" * 30)
                + "\n".join(str(planet) for planet in self.planets)
            )
        planet = self.get_planet(name)
        if not planet:
            return f"Planeta '{name}' não encontrado."
        else:
            return str(planet)

    # 6.3 ▪ total_planets(self): retornar o número de planetas no sistema solar.
    def total_planets(self) -> int:
        """
        Retorna o número total de planetas cadastrados no sistema solar.

        Returns:
            int: Número total de planetas no sistema solar.
        """
        return len(self.planets)

    # 6.4 ▪ total_mass(self): calcular a massa total do sistema solar
    def total_mass(self) -> float:
        """
        Calcula a massa total do sistema solar somando as massas de todos os planetas cadastrados.

        Returns:
            float: Massa total do sistema solar em kg.
        """
        return sum(planet.mass for planet in self.planets)
