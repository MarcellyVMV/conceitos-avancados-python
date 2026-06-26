from pathlib import Path


# 4. Escreva uma função que recebe uma tupla(nome, idade, altura)). Esses dados devem ser escritos no arquivo people.csv.
def store_personal_data(person: tuple) -> None:
    """
    Armazena dados pessoais em people.csv no formato:
    nome;idade;altura

    Args:
        person (tuple): Tupla contendo dados pessoais.
    """
    file_path = Path(__file__).resolve().parent.parent / "assets" / "people.csv"
    with open(file_path, "a", encoding="utf-8") as file:
        name, age, height = person
        file.write(f"{name};{age};{height}\n")
        print(
            f"\nDados armazenados com sucesso em: ~/lista_06_manipulacao_de_arquivos/assets/people.csv"
        )


if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))
    store_personal_data(("Marcelly Victória", 20, 160.0))
