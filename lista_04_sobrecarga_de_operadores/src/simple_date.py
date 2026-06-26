from __future__ import annotations


# 2.I. Implemente a classe SimpleDate, que permite manipular datas. Para simplificar, vamos assumir que cada mês tem 30 dias.(...) Implemente o esboço com métodos que permitam comparações com os operadores <, >, == e !=.
class SimpleDate:
    """
    Representa uma data simples com dia, mês e ano.

    Attributes:
        day (int): Dia da data.
        month (int): Mês da data.
        year (int): Ano da data.
    """

    def __init__(self, day: int, month: int, year: int) -> None:
        """
        Inicializa uma nova data com o dia, mês e ano fornecidos.

        Args:
            day (int): Dia da data.
            month (int): Mês da data.
            year (int): Ano da data.
        """
        if (
            not isinstance(day, int)
            or not isinstance(month, int)
            or not isinstance(year, int)
        ):
            raise TypeError("Dia, mês e ano devem ser inteiros.")
        if day < 1 or day > 30:
            raise ValueError("O dia deve estar entre 1 e 30.")
        if month < 1 or month > 12:
            raise ValueError("O mês deve estar entre 1 e 12.")
        if year < 0:
            raise ValueError("O ano deve ser maior que 0.")
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        """
        Retorna a data no formato DD.MM.AAAA

        Returns:
            str: Data no formato DD.MM.AAAA
        """
        return f"{self.day:02d}.{self.month:02d}.{self.year:04d}"

    def __repr__(self) -> str:
        """
        Retorna a representação oficial da data.

        Returns:
            str: Representação oficial da data.
        """
        return f"SimpleDate(day={self.day}, month={self.month}, year={self.year})"

    def __eq__(self, other: SimpleDate) -> bool:
        """
        Compara se duas datas são iguais.

        Args:
            other (SimpleDate): Segunda data a ser comparada.

        Returns:
            bool: True se as datas forem iguais, False caso contrário.
        """
        if not isinstance(other, SimpleDate):
            return NotImplemented
        return self.total_days() == other.total_days()

    def __ne__(self, other: SimpleDate) -> bool:
        """
        Compara se duas datas são diferentes.

        Args:
            other (SimpleDate): Segunda data a ser comparada.

        Returns:
            bool: True se as datas forem diferentes, False caso contrário.
        """
        if not isinstance(other, SimpleDate):
            return NotImplemented
        return self.total_days() != other.total_days()

    def __lt__(self, other: SimpleDate) -> bool:
        """
        Compara se a data é menor que outra.

        Args:
            other (SimpleDate): A outra data a ser comparada.

        Returns:
            bool: True se a data for menor, False caso contrário.
        """
        if not isinstance(other, SimpleDate):
            return NotImplemented
        return self.total_days() < other.total_days()

    def __gt__(self, other: SimpleDate) -> bool:
        """
        Compara se a data é maior que outra.

        Args:
            other (SimpleDate): Segunda data a ser comparada.

        Returns:
            bool: True se a data for maior, False caso contrário.
        """
        if not isinstance(other, SimpleDate):
            return NotImplemented
        return self.total_days() > other.total_days()

    # 2.II. Implemente o operador de adição +, que permite adicionar um determinado número de dias a um objeto SimpleDate. O operador deve retornar um novo objeto SimpleDate. O objeto original não deve ser alterado.
    def __add__(self, days: int) -> SimpleDate:
        """
        Adiciona um número de dias à data, retornando uma nova data resultante.

        Args:
            days (int): Quantidade de dias a serem adicionados.

        Returns:
            SimpleDate: Nova data resultante da soma.
        """
        if not isinstance(days, int):
            return NotImplemented

        total_days = self.date_in_days() + days
        new_year = total_days // 360
        remaining_days = total_days % 360
        new_month = (remaining_days // 30) + 1
        new_day = (remaining_days % 30) + 1

        return SimpleDate(new_day, new_month, new_year)

    # 2.III. Implemente o operador de subtração -, que permite descobrir a diferença em dias entre dois objetos SimpleDate.
    def __sub__(self, other: SimpleDate) -> int:
        """
        Calcula a diferença em dias entre duas datas.

        Args:
            other (SimpleDate): Segunda data a ser comparada.

        Returns:
            int: Diferença em dias entre as duas datas.
        """
        if not isinstance(other, SimpleDate):
            return NotImplemented
        return self.total_days() - other.total_days()

    def total_days(self) -> int:
        """
        Converte a data para o número total de dias desde o início do calendário.

        Returns:
            int: Número total de dias desde o início do calendário.
        """
        return self.year * 360 + (self.month - 1) * 30 + (self.day - 1)


def main():
    # Exemplo
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(f"\nd1 é: {d1}")  # Output: 04.10.2020
    print(f"d2 é: {d2}")  # Output: 28.12.1985
    print(f"d3 é: {d3}")  # Output: 28.12.1985

    print(f"\nd1 e d2 são Iguais? {'Sim' if d1 == d2 else 'Não'}")  # Output: Não
    print(f"d1 e d2 são Diferentes? {'Sim' if d1 != d2 else 'Não'}")  # Output: Sim
    print(f"d1 e d3 são Iguais? {'Sim' if d1 == d3 else 'Não'}")  # Output: Não
    print(f"d1 é menor que d2? {'Sim' if d1 < d2 else 'Não'}")  # Output: Não
    print(f"d1 é maior que d2? {'Sim' if d1 > d2 else 'Não'}")  # Output: Sim

    d4 = d1 + 3
    d5 = d2 + 400

    print(f"\nd1 + 3 dias é a data(d4): {d4}")  # Output: 07.10.2020
    print(f"d2 + 400 dias é a data(d5): {d5}")  # Output: 08.02.1987

    d6 = SimpleDate(2, 11, 2020)
    print(f"d6 é: {d6}")  # Output: 02.11.2020

    print(f"\nA diferença entre d1 e d6 é de {d1-d6} dias")  # Output: -28
    print(f"A diferença entre d6 e d1 é de {d6-d1} dias")  # Output: 28
    print(f"A diferença entre d1 e d3 é de {d1-d3} dias\n")  # Output: 12516# Exemplo
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(f"\nd1 é: {d1}")  # Output: 04.10.2020
    print(f"d2 é: {d2}")  # Output: 28.12.1985
    print(f"d3 é: {d3}")  # Output: 28.12.1985

    print(f"\nd1 e d2 são Iguais? {'Sim' if d1 == d2 else 'Não'}")  # Output: Não
    print(f"d1 e d2 são Diferentes? {'Sim' if d1 != d2 else 'Não'}")  # Output: Sim
    print(f"d1 e d3 são Iguais? {'Sim' if d1 == d3 else 'Não'}")  # Output: Não
    print(f"d1 é menor que d2? {'Sim' if d1 < d2 else 'Não'}")  # Output: Não
    print(f"d1 é maior que d2? {'Sim' if d1 > d2 else 'Não'}")  # Output: Sim

    d4 = d1 + 3
    d5 = d2 + 400

    print(f"\nd1 + 3 dias é a data(d4): {d4}")  # Output: 07.10.2020
    print(f"d2 + 400 dias é a data(d5): {d5}")  # Output: 08.02.1987

    d6 = SimpleDate(2, 11, 2020)
    print(f"d6 é: {d6}")  # Output: 02.11.2020

    print(f"\nA diferença entre d1 e d6 é de {d1-d6} dias")  # Output: -28
    print(f"A diferença entre d6 e d1 é de {d6-d1} dias")  # Output: 28
    print(f"A diferença entre d1 e d3 é de {d1-d3} dias\n")  # Output: 12516

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
