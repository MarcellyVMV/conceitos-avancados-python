# 2. Desenvolva um sistema de gerenciamento de veículos em uma oficina mecânica. Crie um conjunto de classes usando herança para representar diferentes tipos de veículos e suas funcionalidades.


# I. Crie uma classe chamada Vehicle que tenha os seguintes atributos [brand, model, year e mileage] e métodos[display_info()].
class Vehicle:
    """
    Representa um veículo genérico com atributos comuns a todos os tipos de veículos.

    Attributes:
        brand (str): Marca do veículo.
        model (str): Modelo do veículo.
        year (int): Ano de fabricação do veículo.
        mileage (int): Quilometragem do veículo.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: int) -> None:
        """
        Inicializa um novo veículo com suas características básicas.

        Args:
            brand (str): Marca do veículo.
            model (str): Modelo do veículo.
            year (int): Ano de fabricação do veículo.
            mileage (int): Quilometragem do veículo.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self) -> str:
        """
        Retorna uma representação textual do veículo.

        Returns:
            str: Informações do veículo.
        """
        return (
            f"\nVeículo: {self.brand} {self.model}\n"
            f"Ano: {self.year}\n"
            f"Quilometragem: {self.mileage} km"
        )

    def display_info(self) -> None:
        """
        Exibe as informações do veículo utilizando sua representação textual.
        """
        print(self)


# II. Crie a subclasse Car que herdam de Vehicle. Com um atributo exclusivo [doors]. Obs.: o método display_info() deve ser sobrescrito.
class Car(Vehicle):
    """
    Representa um carro, herdando as características de 'Vehicle' e adicionando atributos específicos como a quantidade de portas.

    Attributes:
        doors (int): Quantidade de portas do carro.
    """

    def __init__(
        self, brand: str, model: str, year: int, mileage: int, doors: int
    ) -> None:
        """
        Inicializa um novo carro com suas características.

        Args:
            brand (str): Marca do carro.
            model (str): Modelo do carro.
            year (int): Ano de fabricação do carro.
            mileage (int): Quilometragem do carro.
            doors (int): Quantidade de portas do carro.
        """
        super().__init__(brand, model, year, mileage)
        self.doors = doors

    def __str__(self) -> str:
        """
        Retorna uma representação textual do carro, incluindo a quantidade de portas.

        Returns:
            str: Informações do carro.
        """
        return super().__str__() + f"\nPortas: {self.doors}"


# II. Crie a subclasses Motorcycle que herdam de Vehicle. Com um atributo exclusivo [has_sidecar (booleano)]. Obs.: o método display_info() deve ser sobrescrito.
class Motorcycle(Vehicle):
    """
    Representa uma motocicleta, herdando as características de 'Vehicle' e adicionando atributos específicos como a presença de um sidecar.

    Attributes:
        has_sidecar (bool): Indica se a motocicleta possui sidecar.
    """

    def __init__(
        self, brand: str, model: str, year: int, mileage: int, has_sidecar: bool
    ) -> None:
        """
        Inicializa uma nova motocicleta com suas características.

        Args:
            brand (str): Marca da motocicleta.
            model (str): Modelo da motocicleta.
            year (int): Ano de fabricação da motocicleta.
            mileage (int): Quilometragem da motocicleta.
            has_sidecar (bool): Indica se a motocicleta possui sidecar.
        """
        super().__init__(brand, model, year, mileage)
        self.has_sidecar = has_sidecar

    def __str__(self) -> str:
        """
        Retorna uma representação textual da motocicleta, incluindo a informação sobre o sidecar.

        Returns:
            str: Informações da motocicleta.
        """
        return super().__str__() + f"\nSidecar: {'Sim' if self.has_sidecar else 'Não'}"


# III. Crie uma subclasse adicional chamada ElectricCar, que herda de Car. Com um atributo exclusivo [battery_capacity] e um método exclusivo [charge()]
class ElectricCar(Car):
    """
    Representa um carro elétrico, que é um tipo específico de carro, com atributos adicionais como a capacidade da bateria.

    Attributes:
        battery_capacity (float): Capacidade da bateria em kWh.
    """

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        mileage: int,
        doors: int,
        battery_capacity: float,
    ) -> None:
        """
        Inicializa um novo carro elétrico com suas características.

        Args:
            brand (str): Marca do carro elétrico.
            model (str): Modelo do carro elétrico.
            year (int): Ano de fabricação do carro elétrico.
            mileage (int): Quilometragem do carro elétrico.
            doors (int): Quantidade de portas do carro elétrico.
            battery_capacity (float): Capacidade da bateria em kWh.
        """
        super().__init__(brand, model, year, mileage, doors)
        self.battery_capacity = battery_capacity

    def __str__(self) -> str:
        """
        Retorna uma representação textual do carro elétrico, incluindo a capacidade da bateria.

        Returns:
            str: Informações do carro elétrico.
        """
        return (
            super().__str__() + f"\nCapacidade da Bateria: {self.battery_capacity} kWh"
        )

    def charge(self) -> None:
        """
        Simula o carregamento do carro elétrico, exibindo uma mensagem indicando que o veículo está sendo carregado.
        """
        print(f"\n\033[1mCarro elétrico {self.brand} {self.model} carregando...\033[0m")


# IV. Crie objetos das três classes (Car, Motorcycle e ElectricCar) e chame seus métodos.
if __name__ == "__main__":
    # Exemplo
    car = Car("Toyota", "Corolla", 2015, 60000, 4)
    car.display_info()

    bike = Motorcycle("Harley-Davidson", "Sportster", 2018, 12000, False)
    bike.display_info()

    electric_car = ElectricCar("BYD", "Dolphin Plus", 2024, 15000, 4, 60.5)
    electric_car.display_info()

    electric_car.charge()
