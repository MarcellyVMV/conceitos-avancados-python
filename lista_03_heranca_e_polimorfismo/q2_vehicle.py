class Vehicle:
    #Função inicial
    def __init__(self, brand, model, year, mileage) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    #Função de exibição
    def display_info(self) -> None:
        print(f"Veículo: {self.brand} {self.model}\nAno: {self.year}\nQuilometragem: {self.mileage} km")

class Car(Vehicle):
    #Função inicial
    def __init__(self, brand, model, year, mileage, doors) -> None:
        super().__init__(brand, model, year, mileage)
        self.doors = doors

    #Função de exibição
    def display_info(self) -> None:
        super().display_info()
        print(f"Portas: {self.doors}")

class Motorcycle(Vehicle):
    #Função inicial
    def __init__(self, brand, model, year, mileage, has_sidecar:bool) -> None:
        super().__init__(brand, model, year, mileage)
        self.has_sidecar = has_sidecar

    #Função de exibição
    def display_info(self) -> None:
        super().display_info()
        print(f"Sidecar: {'Sim' if self.has_sidecar else 'Não'}")

class ElectricCar(Car):
    #Função inicial
    def __init__(self, brand, model, year, mileage, doors, battery_capacity) -> None:
        super().__init__(brand, model, year, mileage, doors)
        self.battery_capacity = battery_capacity

    #Função de exibição
    def display_info(self) -> None:
        super().display_info()
        print(f"Capacidade da Bateria: {self.battery_capacity} kWh")

    #Função de carregamento
    def charge(self) -> None:
        print("\nCarro elétrico carregando...")

# Exemplo
car = Car("Toyota", "Corolla", 2015, 60000, 4)
car.display_info()

bike = Motorcycle("Harley-Davidson", "Sportster", 2018, 12000, False)
bike.display_info()

electric_car = ElectricCar("BYD", "Dolphin Plus", 2024, 15000, 4, 60.5)
electric_car.display_info()

electric_car.charge()