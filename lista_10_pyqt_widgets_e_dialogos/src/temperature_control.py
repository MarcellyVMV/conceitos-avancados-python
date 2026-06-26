from PyQt6.QtCore import Qt, QSize
import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw


# 1. Crie uma aplicação de controle de temperatura de uma geladeira, iniciando em -14°C, com limites de -18°C a -8°C. Deve ter botões para aumentar e diminuir a temperatura em 2ºC, respeitando os limites e exibindo alertas em uma QMessageBox quando forem atingidos.
class TemperatureControl(qtw.QMainWindow):
    """
    Representa a janela principal do controle de temperatura da geladeira.
    """

    WINDOW_TITLE = "Controle de Temperatura da Geladeira"

    MIN_TEMP = -18
    MAX_TEMP = -8
    STEP = 2
    INITIAL_TEMP = -14

    def __init__(self) -> None:
        """
        Inicializa a janela principal do controle de temperatura da geladeira.
        """
        super().__init__()

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setFixedSize(QSize(350, 100))

        self.temperature = self.INITIAL_TEMP
        self.init_ui()

    def init_ui(self) -> None:
        """
        Inicializa a interface gráfica do controle de temperatura da geladeira.
        """
        toolbar = qtw.QToolBar()
        toolbar.setMovable(False)
        toolbar.toggleViewAction().setEnabled(False)
        self.addToolBar(toolbar)

        font = qtg.QFont()
        font.setPointSize(20)

        spacer_left = qtw.QWidget()
        spacer_left.setSizePolicy(
            qtw.QSizePolicy.Policy.Expanding, qtw.QSizePolicy.Policy.Expanding
        )
        toolbar.addWidget(spacer_left)

        # Botão para Aumentar a Temperatura
        increase_action = qtg.QAction("+", self)
        increase_action.setFont(font)
        increase_action.setShortcut("Ctrl+Up")
        increase_action.triggered.connect(self.increase_temperature)
        toolbar.addAction(increase_action)

        # Botão para Resetar a Temperatura
        set_action = qtg.QAction("Setar Temperatura", self)
        set_action.triggered.connect(self.set_temperature)
        toolbar.addAction(set_action)

        # Botão para Diminuir a Temperatura
        decrease_action = qtg.QAction("-", self)
        decrease_action.setFont(font)
        decrease_action.setShortcut("Ctrl+Down")
        decrease_action.triggered.connect(self.decrease_temperature)
        toolbar.addAction(decrease_action)

        spacer_right = qtw.QWidget()
        spacer_right.setSizePolicy(
            qtw.QSizePolicy.Policy.Expanding, qtw.QSizePolicy.Policy.Expanding
        )
        toolbar.addWidget(spacer_right)

        # Rótulo para exibir a temperatura atual
        font = qtg.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.temp_label = qtw.QLabel(f"Temperatura Atual: {self.temperature}°C")
        self.temp_label.setFont(font)
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.temp_label)

    def increase_temperature(self) -> None:
        """
        Aumenta a temperatura em 2ºC.
        """
        if self.temperature < self.MAX_TEMP:
            self.temperature = min(self.temperature + self.STEP, self.MAX_TEMP)
            self.update_display()
        else:
            qtw.QMessageBox.warning(
                self,
                "Aviso!",
                "Temperatura mínima atingida! Não é possível aumentar mais.",
            )

    def decrease_temperature(self) -> None:
        """
        Diminui a temperatura em 2ºC.
        """
        if self.temperature > self.MIN_TEMP:
            self.temperature = max(self.temperature - self.STEP, self.MIN_TEMP)
            self.update_display()
        else:
            qtw.QMessageBox.warning(
                self,
                "Aviso!",
                "Temperatura mínima atingida! Não é possível diminuir mais.",
            )

    # 2. Acrescente ao código do Exercício 1 um novo botão (QpushButton) que permita ao usuário setar diretamente uma nova temperatura a partir de uma caixa de diálogo (QInputDialog).
    def set_temperature(self) -> None:
        """
        Abre uma caixa de diálogo para permitir ao usuário definir uma nova temperatura.
        """
        new_temp, ok = qtw.QInputDialog.getInt(
            self,
            "Definir Temperatura",
            "Insira a nova temperatura (entre -18°C e -8°C):",
            self.temperature,
            self.MIN_TEMP,
            self.MAX_TEMP,
            1,
        )
        if ok:
            self.temperature = new_temp
            self.update_display()

    def update_display(self) -> None:
        """
        Atualiza a exibição da temperatura na interface gráfica.
        """
        self.temp_label.setText(f"Temperatura Atual: {self.temperature}°C")
        print(f"Temperatura ajustada para: {self.temperature}°C")


def main() -> int:
    app = qtw.QApplication([])
    window = TemperatureControl()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
