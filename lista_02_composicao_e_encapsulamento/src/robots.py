# 1. Crie uma classe Robot em que cada robô é identificado pelo seu nome e possui dois métodos: introduce e remove.
class Robot:
    """
    Representa um robô.

    Attributes:
        name (str): Nome do robô.
        active_robots (list): Lista de robôs ativos.
    """

    active_robots = []

    def __init__(self, name: str) -> None:
        """
        Inicializa um robô com seu nome, adicionando-o à lista de robôs ativos.

        Args:
            name (str): Nome do robô.
        """
        self.name = name
        Robot.active_robots.append(self)

    def __str__(self) -> str:
        """
        Retorna uma representação em string do robô.

        Returns:
            str: Representação em string do robô.
        """
        return (
            f"Robô: {self.name}"
            f"Status: {'Ativo' if self in Robot.active_robots else 'Inativo'}"
        )

    # 1.1 O método introduce deve imprimir o nome do robô.
    def introduce(self) -> None:
        """
        Apresenta o robô, imprimindo seu nome.
        """
        print(f"Eu sou o robô {self.name}\n")

    # 1.2 O método remove deve diminuir o número de robôs ativos e imprimir uma mensagem apropriada, dependendo se ainda há robôs ativos ou não.
    def remove(self) -> None:
        """
        Remove o robô da lista de robôs ativos e imprime uma mensagem.
        """
        if self in Robot.active_robots:
            Robot.active_robots.remove(self)
            print(f"Robô {self.name} removido com sucesso.\n")
            if Robot.active_robots:
                print(f"Ainda há {len(Robot.active_robots)} robô(s) ativo(s).\n")
            else:
                print(f"Não existem mais robôs ativos.\n")
        else:
            print(f"Robô {self.name} não encontrado.\n")

    @classmethod  # Métodos da classe
    def print_active_robots(cls) -> None:
        """
        Imprime a quantidade de robôs ativos.
        """
        if Robot.active_robots:
            print(f"Existem {len(cls.active_robots)} robôs ativos.\n")
        else:
            print("Não existem robôs ativos.\n")

    @classmethod
    def list_active_robots(cls) -> None:
        """
        Imprime os nomes dos robôs ativos.
        """
        if Robot.active_robots:
            print("Robôs ativos:")
            for robot in Robot.active_robots:
                print(f"- {robot.name}")
            print()
        else:
            print("Não existem robôs ativos.\n")


if __name__ == "__main__":
    # Exemplo
    robot1 = Robot("Robot1")
    robot2 = Robot("Robot2")

    robot1.introduce()
    robot2.introduce()

    robot1.print_active_robots()
    Robot.print_active_robots()
    Robot.list_active_robots()

    robot1.remove()
    robot1.remove()

    Robot.print_active_robots()
