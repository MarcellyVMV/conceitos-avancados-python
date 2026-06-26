import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw


# 2. Considere o exemplo do jogo da velha da lista anterior. Modifique o jogo para que seja possível importar um jogo já começado e continuar. Vamos considerar que isso seja feito a partir da importação de um arquivo no seguinte formato: Primeira linha é um único carácter indicando o primeiro jogador: ‘X’ ou ‘O’; As outras linhas são as jogadas. Considere que o tabuleiro seja representado de modo que cada linha corresponda a um número de 1 a 3 e cada coluna por uma letra de A a C.
class TicTacToe(qtw.QMainWindow):
    """
    Representa o jogo da velha.
    """

    BOARD_SIZE = 3
    BUTTON_SIZE = 100
    FONT_SIZE = 30

    def __init__(self) -> None:
        """
        Inicializa o jogo da velha.
        """
        super().__init__()

        self.setWindowTitle("Jogo da Velha")
        self.current_player = "X"
        self.moves_count = 0

        self.init_ui()

    def init_ui(self) -> None:
        """
        Inicializa a interface gráfica do jogo da velha.
        """
        # ToolBar
        self.toolbar = qtw.QToolBar("Barra de Ferramentas")
        self.addToolBar(self.toolbar)

        # Ação Import
        self.import_action = qtg.QAction(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DirOpenIcon),
            "Importar Jogo",
            self,
        )
        self.import_action.triggered.connect(self.import_match)
        self.toolbar.addAction(self.import_action)

        # Cria a grade
        grid = qtw.QGridLayout()

        # Cria um Widget genérico para que a gente possa criar nossa grade nele
        central_widget = qtw.QWidget()
        central_widget.setLayout(grid)

        self.setCentralWidget(central_widget)

        # Cria os 9 botões, que representam cada célula do jogo
        self.buttons: list[list[qtw.QPushButton]] = [
            [qtw.QPushButton("") for _ in range(self.BOARD_SIZE)]
            for _ in range(self.BOARD_SIZE)
        ]

        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                button = self.buttons[row][col]
                button.setFixedSize(self.BUTTON_SIZE, self.BUTTON_SIZE)
                font = qtg.QFont()
                font.setPointSize(self.FONT_SIZE)
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
        button = self.buttons[row][col]
        # Checa se a célula está preenchida
        if button.text():
            return

        button.setText(self.current_player)
        self.moves_count += 1

        # Checa se houve vitória (escrever uma mensagem descritiva)
        if self.check_win():
            qtw.QMessageBox.information(
                self, "Vitória!", f"Jogador {self.current_player} venceu!"
            )
            self.close()
            return

        # Checa se houve empate (escrever uma mensagem descritiva)
        if self.moves_count == 9:
            qtw.QMessageBox.information(self, "Empate", "O jogo terminou em empate!")
            self.close()
            return

        self.switch_player()

    def check_win(self) -> bool:
        """
        Verifica linhas, colunas e diagonais para checar se houve vitória.

        Returns:
            bool: True se houve vitória, False caso contrário
        """
        board = [[button.text() for button in row] for row in self.buttons]
        for i in range(self.BOARD_SIZE):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return True
            if board[0][i] == board[1][i] == board[2][i] != "":
                return True
        if board[0][0] == board[1][1] == board[2][2] != "":
            return True
        if board[0][2] == board[1][1] == board[2][0] != "":
            return True
        return False

    def import_match(self) -> None:
        """
        Importa um jogo salvo em um arquivo de texto.
        """

        # Importa o jogo
        path, _ = qtw.QFileDialog.getOpenFileName(
            self, "Importar Jogo", "", "Arquivos de Texto (*.txt)"
        )
        if not path:
            return

        self.reset_board()

        try:
            with open(path, "r", encoding="utf-8") as file:
                lines = lines = [line.strip() for line in file]

                if not lines:
                    raise ValueError("Arquivo vazio.")
                if len(lines) < 2:
                    raise ValueError("Arquivo inválido.")
                if len(lines) - 1 > 9:
                    raise ValueError("O jogo possui mais de 9 jogadas.")

                self.current_player = lines[0]
                if self.current_player not in ["X", "O"]:
                    raise ValueError("Jogador inicial inválido. Deve ser 'X' ou 'O'.")

                for move in lines[1:]:
                    move = move.upper()
                    if len(move) != 2 or move[0] not in "ABC" or move[1] not in "123":
                        raise ValueError(f"Jogada inválida: {move}")

                    row = int(move[1]) - 1
                    col = ord(move[0]) - ord("A")
                    if self.buttons[row][col].text() != "":
                        raise ValueError(f"Posição {move} já está preenchida.")

                    self.buttons[row][col].setText(self.current_player)
                    self.moves_count += 1

                    self.switch_player()

                if self.check_win():
                    raise ValueError("O jogo importado já possui um vencedor.")

            qtw.QMessageBox.information(
                self, "Importação Concluída", "Jogo importado com sucesso!"
            )

        except (FileNotFoundError, ValueError, OSError) as e:
            qtw.QMessageBox.warning(
                self, "Erro de Importação", f"Erro ao importar jogo: {e}"
            )

    # Funções auxiliares
    def reset_board(self) -> None:
        """
        Limpa o tabuleiro e reinicia o jogo.
        """
        for row in self.buttons:
            for button in row:
                button.setText("")
        self.moves_count = 0
        self.current_player = "X"

    def switch_player(self) -> None:
        """
        Alterna o jogador atual.
        """
        self.current_player = "X" if self.current_player == "O" else "O"


def main() -> int:
    app = qtw.QApplication([])
    game = TicTacToe()
    game.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
