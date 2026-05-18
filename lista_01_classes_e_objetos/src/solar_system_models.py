from math import pi, sqrt


# 5. Crie uma classe Moon que represente uma lua de um Planeta.
class Moon:
    """
    Representa uma lua de um planeta.
    """

    def __init__(self, name: str, diameter: float, distance_from_planet: float) -> None:
        """
        Inicializa uma lua com o nome, diâmetro e distância do planeta.

        Args:
            name (str): O nome da lua.
            diameter (float): O diâmetro da lua em km.
            distance_from_planet (float): A distância da lua ao planeta em km.
        """
        self.name = name
        self.diameter = diameter
        self.distance_from_planet = distance_from_planet

    def __str__(self) -> str:
        """
        Retorna uma representação em string da lua.

        Returns:
            str: A representação em string da lua.
        """
        return (
            f"Lua: {self.name}\n"
            f"Diâmetro: {self.diameter:.2f} km\n"
            f"Distância do Planeta: {self.distance_from_planet:.2f} km\n"
        )


# 1. Crie uma classe chamada Planet que represente um planeta do sistema solar.
class Planet:
    """
    Representa um planeta do sistema solar.
    """

    # Constantes
    G = 6.674e-11
    SUN_MASS = 1.989e30

    def __init__(
        self, name: str, mass: float, diameter: float, distance_from_sun: float
    ) -> None:
        """
        Inicializa um planeta com o nome, massa, diâmetro e distância do Sol.

        Args:
            name (str): O nome do planeta.
            mass (float): A massa do planeta em kg.
            diameter (float): O diâmetro do planeta em km.
            distance_from_sun (float): A distância do planeta ao Sol em km.
        """
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.distance_from_sun = distance_from_sun
        # 5.1 ▪ Adicione um novo atributo à classe Planet denominado moons, que deve ser uma lista de objetos do tipo Moon.
        self.moons: list[Moon] = []

    # 2. Adicione a sua classe do exercício (1), um método describe, que imprima os detalhes do Planeta.
    # def describe(self) -> str:
    #    return (f"Planeta: {self.name}\nMassa: {self.mass:.2e} kg\nDiâmetro: {self.diameter:.2f} km\n"
    #        f"Distância do Sol: {self.distance_from_sun:.2f} km\n")

    # 3. Substitua o método describe do exercício anterior pelo método especial __str__.
    def __str__(self) -> str:
        """
        Retorna uma representação em string do planeta.

        Returns:
            str: A representação em string do planeta.
        """
        return (
            f"Planeta: {self.name}\n"
            f"Massa: {self.mass:.2e} kg\n"
            f"Diâmetro: {self.diameter:.2f} km\n"
            f"Distância do Sol: {self.distance_from_sun:.2f} km\n"
        )

    # 4. Crie um método para calcular e retornar o período orbital do planeta.
    def orbital_period(self) -> float:
        """
        Calcula e retorna o período orbital do planeta.

        Returns:
            float: O período orbital do planeta.
        """
        # km -> m
        radius_meters = self.distance_from_sun * 1000
        # Período em segundos
        period_seconds = (
            2 * pi * sqrt((radius_meters**3) / (Planet.G * Planet.SUN_MASS))
        )
        # s -> anos
        period_years = period_seconds / (365.25 * 24 * 3600)
        return period_years

    # 5.2 ▪ Adicione um método add_moon( self, moon) que receba um objeto Moon como parâmetro e o adicione à lista de luas (moons).
    def add_moon(self, moon: Moon) -> None:
        """
        Adiciona uma lua ao planeta.

        Args:
            moon (Moon): A lua a ser adicionada ao planeta.
        """
        self.moons.append(moon)

    # 5.3 ▪ Crie um método describe_moons, que chame o método __str__ de cada uma das suas luas.
    def describe_moons(self) -> str:
        """
        Descreve as luas do planeta.

        Returns:
            str: As luas do planeta.
        """
        if not self.moons:
            return "Nenhuma lua cadastrada."
        return "Luas cadastradas:\n" + "\n".join(str(moon) for moon in self.moons)


# 6. Crie uma classe SolarSystem que represente um sistema solar.
class SolarSystem:
    """
    Representa um sistema solar.
    """

    def __init__(self) -> None:
        """
        Inicializa um objeto SolarSystem.
        """
        self.planets: list[Planet] = []

    # 6.1 ▪ add_planet(self, planet): adicionar um objeto Planet à lista de planetas (planets).
    def add_planet(self, planet: Planet) -> None:
        """
        Adiciona um planeta ao sistema solar.

        Args:
            planet (Planet): O planeta a ser adicionado ao sistema solar.
        """
        self.planets.append(planet)

    # 6.2 ▪ describe(self, name=0): se for fornecido um nome, descreve os detalhes do planeta específico com o nome. Caso contrário, escreve os detalhes de todos os planetas.
    def describe_planets(self, name: str = None) -> str:
        """
        Descreve os detalhes dos planetas.

        Args:
            name (str): O nome do planeta para o qual deseja-se obter os detalhes.

        Returns:
            str: Os detalhes dos planetas.
        """
        if name is None:
            if not self.planets:
                return "Nenhum planeta cadastrado."
            return "Planetas cadastrados:\n" + "\n".join(
                str(planet) for planet in self.planets
            )
        if not self.planets:
            return "Nenhum planeta cadastrado."
        for planet in self.planets:
            if planet.name.lower() == name.lower():
                return str(planet)
        return f"Planeta {name} não encontrado."

    # 6.3 ▪ total_planets(self): retornar o número de planetas no sistema solar.
    def total_planets(self) -> int:
        """
        Retorna o número de planetas no sistema solar.

        Returns:
            int: O número de planetas no sistema solar.
        """
        return len(self.planets)

    # 6.4 ▪ total_mass(self): calcular a massa total do sistema solar
    def total_mass(self) -> float:
        """
        Calcula a massa total do sistema solar.

        Returns:
            float: A massa total do sistema solar.
        """
        return sum(planet.mass for planet in self.planets)
