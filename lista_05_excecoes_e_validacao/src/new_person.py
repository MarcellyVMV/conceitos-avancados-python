# 1. Escreva uma função que cria e retorna uma tupla (nome, idade) validando os dados: nome não pode ser vazio, deve ter pelo menos duas palavras e no máximo 40 caracteres; idade deve estar entre 0 e 150. Caso contrário, lança ValueError.
def new_person(name: str, age: int) -> tuple[str, int]:
    """
    Cria e retorna uma tupla contendo o nome e a idade de uma pessoa.

    Args:
        name (str): Nome da pessoa.
        age (int): Idade da pessoa.

    Returns:
        tuple[str, int]: Tupla contendo o nome e a idade da pessoa.
    """
    if not name.strip():
        raise ValueError("Nome inválido: o nome não pode ser vazio.")
    if len(name.split()) < 2:
        raise ValueError("Nome inválido: o nome deve conter pelo menos 2 palavras.")
    if len(name) > 40:
        raise ValueError("Nome inválido: o nome deve ter no máximo 40 caracteres.")
    if age < 0:
        raise ValueError("Idade inválida: a idade não pode ser negativa.")
    if age > 150:
        raise ValueError("Idade inválida: a idade deve ser menor ou igual a 150.")
    return name, age


if __name__ == "__main__":
    tests: list[tuple[str, int]] = [
        ("   ", 20),  # Caso Nome invalido 1
        ("Marcelly", 20),  # Caso Nome invalido 2
        ("Maaaarrrrcellllllyyyyy Viccctórrriiiiiaaa", 20),  # Caso Nome invalido 3
        ("Marcelly Victória", -1),  # Caso Idade invalida
        ("Marcelly Victória", 151),  # Caso Idade invalida
        ("Marcelly Victória", 20),
    ]

    for name, age in tests:
        try:
            person = new_person(name, age)
            print(f"Pessoa criada: {person}")
        except ValueError as e:
            print(f"Erro: {e}")
