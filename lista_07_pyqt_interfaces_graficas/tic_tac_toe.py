from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QPushButton, QMessageBox


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jogo da Velha")
        self.current_player = "X"
        self.moves_count = 0

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
        # Checar se a célula está preenchida
        if self.buttons[row][col].text() != "":
            return
        
        self.buttons[row][col].setText(self.current_player)
        self.moves_count += 1

        # Checar se houve vitória (escrever uma mensagem descritiva)
        if self.check_win():
            QMessageBox.information(self, "Vitória!", f"Jogador {self.current_player} venceu!")
            self.close()
            return

        # Checar se houve empate (escrever uma mensagem descritiva)
        if self.moves_count == 9:
            QMessageBox.information(self, "Empate", "O jogo terminou em empate!")
            self.close()
            return
        
        self.current_player = "X" if self.current_player == "O" else "O"
    
    # Verifica linhas, colunas e diagonais para checar se houve vitória
    def check_win(self):
        for i in range(3):
            if self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() != '':
                return True
            if self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() != '':
                return True
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != '':
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != '':
            return True
        return False

def main():
    app = QApplication([])
    game = TicTacToe()
    game.show()
    app.exec()
    
main()