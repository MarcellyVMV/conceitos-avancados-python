from pathlib import Path


# 5. Escreva uma função chamada filter_solutions() que: Leia o conteúdo do arquivo solutions.csv. Escreva as linhas que têm o resultado correto em correct.csv e, as incorretas, em incorrect.csv.
def filter_solutions() -> None:
    """
    Lê solutions.csv e separa respostas corretas e incorretas.
    """
    base = Path(__file__).resolve().parent.parent / "assets"
    correct_path = base / "correct.csv"
    incorrect_path = base / "incorrect.csv"
    input_path = base / "solutions.csv"

    with open(input_path, "r", encoding="utf-8") as file, open(
        correct_path, "w", encoding="utf-8"
    ) as correct, open(incorrect_path, "w", encoding="utf-8") as incorrect:
        for line in file:
            _, equation, result = line.strip().split(";")
            if solve_expression(equation) == int(result):
                correct.write(line)
            else:
                incorrect.write(line)

    print(f"\nArquivos 'correct.csv' e 'incorrect.csv' criados com sucesso.")


# Função auxiliar
def solve_expression(equation: str) -> float:
    """
    Resolve uma expressão matemática simples contendo dois operandos e um operador (+, -, * ou /).

    Args:
        equation (str): Equação matemática.

    Returns:
        float: Resultado da equação.
    """
    equation = equation.strip()
    if "+" in equation:
        a, b = map(int, equation.split("+"))
        return a + b
    elif "-" in equation:
        a, b = map(int, equation.split("-"))
        return a - b
    elif "*" in equation:
        a, b = map(int, equation.split("*"))
        return a * b
    elif "/" in equation:
        a, b = map(int, equation.split("/"))
        return a / b
    raise ValueError(f"Equação inválida: {equation}")


if __name__ == "__main__":
    filter_solutions()
