from PyQt6.QtCore import QSize, Qt
import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw


class BrightnessControl(qtw.QMainWindow):
    """
    Representa a janela principal do controle de brilho.
    """

    WINDOW_TITLE = "Controle de Brilho"

    STEP = 10
    MIN_BRIGHTNESS = 0
    MAX_BRIGHTNESS = 100
    INITIAL_BRIGHTNESS = 50

    def __init__(self) -> None:
        """
        Inicializa a janela principal do controle de brilho.
        """
        super().__init__()

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setFixedSize(QSize(240, 130))

        self.brightness = self.INITIAL_BRIGHTNESS

        self.init_ui()

    def init_ui(self) -> None:
        """
        Inicializa a interface gráfica do controle de brilho.
        """
        self.central_widget = qtw.QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = qtw.QVBoxLayout()
        buttons_layout = qtw.QHBoxLayout()
        self.central_widget.setLayout(main_layout)

        base_font = qtg.QFont()
        base_font.setPointSize(12)
        base_font.setBold(True)

        # Menu Brilho #
        brightness_menu = self.menuBar().addMenu("Brilho")

        font_button = qtg.QFont(base_font)
        font_button.setPointSize(15)

        self.increase_action = qtg.QAction("Aumentar Brilho", self)
        self.increase_action.setShortcut("Ctrl+Up")
        self.increase_action.triggered.connect(self.increase_brightness)
        brightness_menu.addAction(self.increase_action)
        # Botão Aumentar
        increase_button = qtw.QPushButton("+")
        increase_button.setFixedSize(50, 40)
        increase_button.setFont(font_button)
        increase_button.setToolTip("Aumentar brilho (Ctrl+↑)")
        increase_button.clicked.connect(self.increase_brightness)

        self.decrease_action = qtg.QAction("Diminuir Brilho", self)
        self.decrease_action.setShortcut("Ctrl+Down")
        self.decrease_action.triggered.connect(self.decrease_brightness)
        brightness_menu.addAction(self.decrease_action)
        # Botão Diminuir
        decrease_button = qtw.QPushButton("-")
        decrease_button.setFixedSize(50, 40)
        decrease_button.setFont(font_button)
        decrease_button.setToolTip("Diminuir brilho (Ctrl+↓)")
        decrease_button.clicked.connect(self.decrease_brightness)

        self.reset_action = qtg.QAction("Resetar Brilho", self)
        self.reset_action.setShortcut("Ctrl+R")
        self.reset_action.triggered.connect(self.reset_brightness)
        brightness_menu.addAction(self.reset_action)
        # Botão Reset
        reset_button = qtw.QPushButton()
        reset_button.setIcon(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_BrowserReload)
        )
        reset_button.setFixedSize(40, 40)
        reset_button.setFont(font_button)
        reset_button.setToolTip("Resetar brilho (Ctrl+R)")
        reset_button.clicked.connect(self.reset_brightness)

        # Botões #
        buttons_layout.addStretch()
        buttons_layout.addWidget(increase_button)
        buttons_layout.addWidget(reset_button)
        buttons_layout.addWidget(decrease_button)
        buttons_layout.addStretch()

        # Label Brilho #
        main_layout.addLayout(buttons_layout)

        self.brightness_label = qtw.QLabel(f"Brilho: {self.brightness}%")
        self.brightness_label.setFont(base_font)
        self.brightness_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.brightness_label)

    def increase_brightness(self) -> None:
        """
        Aumenta o brilho da tela em 10%.
        """
        if self.brightness < self.MAX_BRIGHTNESS:
            self.brightness = min(
                self.brightness + self.STEP,
                self.MAX_BRIGHTNESS,
            )
            self.update_brightness_label()
            print(f"Brilho aumentado para: {self.brightness}%")
        else:
            print("Brilho já está no máximo (100%).")

    def decrease_brightness(self) -> None:
        """
        Diminui o brilho da tela em 10%.
        """
        if self.brightness > self.MIN_BRIGHTNESS:
            self.brightness = max(
                self.brightness - self.STEP,
                self.MIN_BRIGHTNESS,
            )
            self.update_brightness_label()
            print(f"Brilho diminuído para: {self.brightness}%")
        else:
            print("Brilho já está no mínimo (0%).")

    def reset_brightness(self) -> None:
        """
        Reseta o brilho da tela para o valor inicial.
        """
        self.brightness = self.INITIAL_BRIGHTNESS
        self.update_brightness_label()
        print(f"Brilho resetado para: {self.brightness}%")

    def update_brightness_label(self) -> None:
        """
        Atualiza o texto do indicador de brilho.
        """
        self.brightness_label.setText(f"Brilho: {self.brightness}%")


def main() -> int:
    app = qtw.QApplication([])
    window = BrightnessControl()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
