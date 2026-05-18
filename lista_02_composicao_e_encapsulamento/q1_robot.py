class Robot:
    #Lista de robôs ativos
    active_robots = []

    #Função inicial
    def __init__(self, name):
        self.name = name
        Robot.active_robots.append(self)

    #Função para mostrar o nome do robo
    def introduce(self):
        print(f"Meu nome é {self.name}")

    #Função para remover o robo
    def remove(self):
        print(f"\n\033[1mRemovendo {self.name}...\033[0m")
        Robot.active_robots.remove(self)

    #Função para mostrar quantos robôs estão ativos
    def print_active_robots():
        print(f"\nHá {len(Robot.active_robots)} robôs ativos.")

# Exemplo
robot1 = Robot("Robo1")
robot2 = Robot("Robo2")

robot1.introduce()
robot2.introduce()

#robot1.print_active_robots()
Robot.print_active_robots()

robot1.remove()
robot2.remove()

#robot1.print_active_robots()
Robot.print_active_robots()