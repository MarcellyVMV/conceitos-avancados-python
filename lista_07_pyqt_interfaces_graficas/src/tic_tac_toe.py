from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QGridLayout,
    QWidget,
    QPushButton,
    QMessageBox,
)


class TicTacToe(QMainWindow):
    """
    Representa o jogo da velha.
    """

    def __init__(self) -> None:
        """
        Inicializa o jogo da velha.
        """
        super().__init__()

        self.setWindowTitle("Jogo da Velha")
        self.current_player = "X"
        self.moves_count = 0
        self.buttons = []

        self.init_ui()

    def init_ui(self) -> None:
        """
        Inicializa a interface gráfica do jogo da velha.
        """
        # Cria a grade
        grid = QGridLayout()

        # Cria um Widget genérico para que a gente possa criar nossa grade nele
        base_widget = QWidget()
        base_widget.setLayout(grid)

        self.setCentralWidget(base_widget)

        # Cria os 9 botões, que representam cada célula do jogo
        self.buttons: list[list[QPushButton]] = [
            [QPushButton("") for _ in range(3)] for _ in range(3)
        ]

        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.setFixedSize(100, 100)
                font = QFont()
                font.setPointSize(30)
                button.setFont(font)
                button.clicked.connect(
                    lambda _, x=row, y=col: self.on_button_clicked(x, y)
                )
                grid.addWidget(button, row, col)

    def on_button_clicked(self, row: int, col: int) -> None:
        """
        Executado quando um botão da grade é clicado.

        Args:
            row (int): Linha da célula clicada
            col (int): Coluna da célula clicada
        """
        # TODO: checar se a célula está preenchida
        if self.buttons[row][col].text() != "":
            return

        self.buttons[row][col].setText(self.current_player)
        self.moves_count += 1

        # TODO: checar se houve vitória (escrever uma mensagem descritiva)
        if self.check_win():
            QMessageBox.information(
                self, "Vitória!", f"Jogador {self.current_player} venceu!"
            )
            self.close()
            return

        # TODO: checar se houve empate (escrever uma mensagem descritiva)
        if self.moves_count == 9:
            QMessageBox.information(self, "Empate", "O jogo terminou em empate!")
            self.close()
            return

        self.current_player = "X" if self.current_player == "O" else "O"

    # Verifica linhas, colunas e diagonais para checar se houve vitória
    def check_win(self) -> bool:
        """
        Verifica se houve vitória.

        Returns:
            bool: True se houve vitória, False caso contrário
        """
        board = [[button.text() for button in row] for row in self.buttons]
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return True
            if board[0][i] == board[1][i] == board[2][i] != "":
                return True
        if board[0][0] == board[1][1] == board[2][2] != "":
            return True
        if board[0][2] == board[1][1] == board[2][0] != "":
            return True
        return False


def main() -> int:
    app = QApplication([])
    game = TicTacToe()
    game.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
