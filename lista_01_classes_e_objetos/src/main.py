from solar_system_models import Moon, Planet, SolarSystem


def main():
    print("\nBem Vindo ao Virtual Solar System!")

    solar_system = SolarSystem()

    while True:
        indice = int(
            input(
                "\nDigite o número da ação que deseja realizar \n"
                "(1-Adicionar Planeta, "
                "2-Adicionar Lua, "
                "3-Exibir Descrição, "
                "4-Exibir número total de planetas e massa total do sistema solar, "
                "0-Sair): \n"
            )
        )

        if indice == 0:
            print("\033[1m\nSaindo...\n\n\033[0m")
            break

        # 7.1 ▪ Permitir que o usuário adicione múltiplos planetas ao sistema solar.
        elif indice == 1:
            planet_name = input("\nDigite o nome do planeta: ")
            planet_mass = float(
                input(f"Digite a massa do planeta {planet_name} (kg): ")
            )
            planet_diameter = float(
                input(f"Digite o diâmetro do planeta {planet_name} (km): ")
            )
            distance_from_sun = float(
                input(f"Digite a distância do planeta {planet_name} ao Sol (km): ")
            )
            planet = Planet(
                planet_name, planet_mass, planet_diameter, distance_from_sun
            )
            solar_system.add_planet(planet)
            print(f"\nPlaneta '{planet_name}' cadastrado com sucesso!")

        # 7.2 ▪ Para cada planeta, permitir que o usuário adicione uma ou mais luas.
        elif indice == 2:
            moon_name = input("\nDigite o nome da Lua: ")
            name_planet = input(
                f"Digite o nome do planeta ao qual a '{moon_name}' orbita: "
            )
            planet = SolarSystem.get_planet(solar_system, name_planet)

            if planet:
                moon_diameter = float(
                    input(f"Digite o diâmetro da lua '{moon_name}' (km): ")
                )
                distance_from_planet = float(
                    input(
                        f"Digite a distância da Lua '{moon_name}' ao Planeta '{name_planet}' (km): "
                    )
                )
                moon = Moon(moon_name, moon_diameter, distance_from_planet)
                planet.add_moon(moon)
                print(f"\nLua '{moon_name}' cadastrada com sucesso!")
            else:
                print("\nPlaneta não encontrado.")

        # 7.2 ▪ Exibir uma descrição de todos os planetas e suas respectivas luas no sistema solar.
        # 7.3 ▪ Permitir que o usuário solicite a descrição detalhada de um planeta específico.
        elif indice == 3:
            name_planet = input(
                "\nDigite o nome do planeta para exibir a descrição ou digite 0 para exibir todas as descrições: "
            )
            if name_planet == "0":
                print()
                print(solar_system.describe())
            else:
                print()
                print(solar_system.describe(name_planet))

        # 7.4 ▪ Exibir o número total de planetas e a massa total do sistema solar.
        elif indice == 4:
            print(f"\nNumero total de planetas: {solar_system.total_planets()}")
            print(f"Massa total do sistema solar: {solar_system.total_mass():.2e} kg")

        else:
            print("\nOpção inválida. Tente novamente.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
