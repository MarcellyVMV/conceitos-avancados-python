from math import pi, sqrt


class Planet:
    # Função inicial
    def __init__(self, name, mass, diameter, distance_from_sun) -> None:
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.distance_from_sun = distance_from_sun
        self.moon = []

    # def describe(self) -> None:
    #   print(f"O Planeta é {self.name}\nA Massa é {str(self.mass) + ' kg'}\nO Diâmetro é {str(self.diameter) + ' km'}/
    #        \nA Distância do Sol é {str(self.distance_from_sun) + ' km'}")

    # Função de descrição
    def __str__(self) -> str:
        return f"\nPlaneta: {self.name}\nMassa: {str(self.mass) + ' kg'}\nDiâmetro: {str(self.diameter) + ' km'}\nDistância do Sol: {str(self.distance_from_sun) + ' km'}"

    # Função que calcula o período orbital
    def orbital_period(self) -> float:
        G = 6.674 * pow(10, -11)
        period = 2 * pi * sqrt(pow(self.distance_from_sun, 3) / (G * self.mass))
        return period

    # Função que adiciona Lua
    def add_moon(self, moon) -> None:
        self.moon.append(moon)


class Moon:
    # Função inicial
    def __init__(self, name, diameter, distance_from_planet) -> None:
        self.name = name
        self.diameter = diameter
        self.distance_from_planet = distance_from_planet

    # Função de descrição
    def __str__(self) -> str:
        return f"Lua: {self.name}\nDiâmetro: {str(self.diameter) + ' km'}\nDistância do Planeta: {str(self.distance_from_planet) + ' km'}"


class SolarSystem:
    # Função inicial
    def __init__(self) -> None:
        self.planets = []

    # Função que adiciona planeta
    def add_planet(self, planet) -> None:
        self.planets.append(planet)

    # Função de descrição
    def describe(self, name=0) -> None:
        if name == 0:
            for planet in self.planets:
                print(planet)
        elif name != 0:
            for planet in self.planets:
                if planet.name == name:
                    print(planet)

    # Função que calcula o número total de planetas
    def total_planets(self) -> int:
        return len(self.planets)

    # Função que calcula a massa total do sistema solar
    def total_mass(self) -> float:
        return sum(planet.mass for planet in self.planets)


# Função principal
def main():
    print("\nBem Vindo ao Virtual Solar System!")
    solar_system = SolarSystem()
    while True:
        indice = int(
            input(
                "\nDigite o número da ação que deseja realizar \n(1-Adicionar Planeta, 2-Adicionar Lua, 3-Exibir Descrição, 4-Exibir número total de planetas e massa total do sistema solar, 0-Sair):\n"
            )
        )
        if indice == 0:
            print("\033[1m\nSaindo...\n\n\033[0m")
            break
        elif indice == 1:
            name = input("\nDigite o nome do planeta: ")
            mass = float(input(f"Digite a massa do planeta {name} (kg): "))
            diameter = float(input(f"Digite o diâmetro do planeta {name} (km): "))
            distance_from_sun = float(
                input(f"Digite a distância do planeta {name} ao Sol (km): ")
            )
            planeta = Planet(name, mass, diameter, distance_from_sun)
            solar_system.add_planet(planeta)
        elif indice == 2:
            name = input("\nDigite o nome da Lua: ")
            namePlanet = input(f"Digite o nome do planeta ao qual a {name} orbita: ")
            diameter = float(input(f"Digite o diâmetro da lua '{name}' (km): "))
            distance_from_planet = float(
                input(
                    f"Digite a distância da Lua '{name}' ao Planeta '{namePlanet}' (km): "
                )
            )
            lua = Moon(name, diameter, distance_from_planet)
            for planet in solar_system.planets:
                if planet.name == namePlanet:
                    planet.add_moon(lua)
        elif indice == 3:
            planet = input(
                "\nDigite o nome do planeta para exibir a descrição ou digite 0 para exibir todas as descrições: "
            )
            if planet != "0":
                solar_system.describe(planet)
            else:
                solar_system.describe()
        elif indice == 4:
            print(f"\nNumero total de planetas: {solar_system.total_planets()}")
            print(f"Massa total do sistema solar: {solar_system.total_mass():.2e} kg")
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Exemplo
# solar_system = SolarSystem()
# earth = Planet("Terra", 6 * 10**24, 12700, 150 * 10**6)
# moon_earth = Moon("Lua", 3475, 384400)
# earth.add_moon(moon_earth)
# solar_system.add_planet(earth)
#
# mars = Planet("Marte", 0.6 * 10**24, 6800, 230 * 10**6)
# fobos_mars = Moon("Fobos", 22.4, 9377)
# deimos_mars = Moon("Deimos", 12.4, 23460)
# mars.add_moon(fobos_mars)
# mars.add_moon(deimos_mars)
# solar_system.add_planet(mars)
#
## Descreve todos os planetas
# solar_system.describe()
# print()
#
## Descreve especificamente a Terra
# solar_system.describe("Terra")
# print(f"Massa total do sistema solar: {solar_system.total_mass():.2e} kg")
# print(f"Numero total de planetas: {solar_system.total_planets()}")
