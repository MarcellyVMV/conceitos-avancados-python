from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QPushButton


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jogo da Velha")
        self.current_player = "X"

        self.initUI()

    def initUI(self):
        # Cria a grade
        grid = QGridLayout()

        # Cria um Widget genérico para que a gente possa criar nossa grade nele
        base_widget = QWidget()
        base_widget.setLayout(grid)

        self.setCentralWidget(base_widget)

        # Cria os 9 botões, que representam cada célula do jogo
        self.buttons = [[QPushButton('') for _ in range(3)] for _ in range(3)]
        
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.setFixedSize(100,100)
                font = QFont()
                font.setPointSize(30)
                button.setFont(font)
                button.clicked.connect(lambda _, x=row, y=col : self.on_button(x, y))
                grid.addWidget(self.buttons[row][col], row, col)

    def on_button(self, row, col):  
        # TODO: checar se a célula está preenchida      
        self.buttons[row][col].setText(self.current_player)
        self.current_player = "X" if self.current_player == "O" else "O"

        # TODO: checar se houve vitória (escrever uma mensagem descritiva)

        # TODO: checar se houve empate (escrever uma mensagem descritiva)

def main():
    app = QApplication([])
    game = TicTacToe()
    game.show()
    app.exec()
    
main()