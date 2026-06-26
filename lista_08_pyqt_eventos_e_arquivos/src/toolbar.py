from pathlib import Path
import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw


# 1. Crie uma aplicação que exibe uma janela principal com uma barra de ferramentas contendo dois ícones: “novo” e “abrir”. (...)
class Toolbar(qtw.QMainWindow):
    """
    Representa a janela principal da aplicação.
    """

    WINDOW_TITLE = "My Toolbar"
    TOOLBAR_NAME = "Barra de Ferramentas"

    def __init__(self) -> None:
        """
        Inicializa a janela principal da aplicação.
        """
        super().__init__()
        self.setWindowTitle(self.WINDOW_TITLE)
        self.init_ui()

    def init_ui(self) -> None:
        """
        Inicializa a interface gráfica da janela.
        """
        self.setCentralWidget(qtw.QWidget())

        # ToolBar
        self.toolbar = qtw.QToolBar(self.TOOLBAR_NAME)
        self.addToolBar(self.toolbar)

        # Ação NOVO
        self.new_action = qtg.QAction(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_FileIcon),
            "Novo",
            self,
        )
        self.new_action.triggered.connect(self.new_file)
        self.toolbar.addAction(self.new_action)

        # Ação ABRIR
        self.open_action = qtg.QAction(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DirOpenIcon),
            "Abrir",
            self,
        )
        self.open_action.triggered.connect(self.open_file)
        self.toolbar.addAction(self.open_action)

    def new_file(self) -> None:
        """
        Cria um novo arquivo.
        """
        name = input("Nome do novo arquivo (sem extensão): ")
        print("Digite o texto para o novo arquivo (digite 'sair' para terminar):")

        content: list[str] = []

        while True:
            line = input()
            if line.lower() == "sair":
                break
            content.append(line)

        path = Path(f"{name}.txt")
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write("\n".join(content))
            qtw.QMessageBox.information(
                self, "Sucesso", f"Arquivo '{path.name}' salvo com sucesso."
            )

        except OSError as e:
            qtw.QMessageBox.critical(
                self, "Erro", f"Não foi possível salvar o arquivo.\n\n{e}"
            )

    def open_file(self) -> None:
        """
        Abre um arquivo existente.
        """
        file_path, _ = qtw.QFileDialog.getOpenFileName(
            self, "Abrir Arquivo", "", "Todos os Arquivos (*)"
        )

        if not file_path:
            return
        path = Path(file_path)
        try:
            with open(path, "r", encoding="utf-8") as file:
                print(file.read())
        except OSError as e:
            qtw.QMessageBox.critical(
                self, "Erro", f"Não foi possível abrir o arquivo.\n\n{e}"
            )


def main() -> int:
    app = qtw.QApplication([])
    window = Toolbar()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
