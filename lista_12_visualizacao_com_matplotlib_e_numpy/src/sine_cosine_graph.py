from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


# 1. Plotar, no mesmo gráfico, as funções seno e cosseno no intervalo [0,2π], com títulos para o gráfico e eixos. A curva do seno deve ser vermelha e contínua, e a do cosseno dourada, pontilhada e com marcadores.
def plot_sine_cosine():
    """
    Plota as funções seno e cosseno no intervalo [0, 2π].
    O gráfico inclui título, legenda, grade e rótulos para os eixos.
    """
    x_values = np.linspace(0, 2 * np.pi, 200)

    sine = np.sin(x_values)
    cosine = np.cos(x_values)

    plt.figure(figsize=(8, 5))

    plt.plot(x_values, sine, label="Seno", color="red")
    plt.plot(
        x_values, cosine, label="Cosseno", color="gold", linestyle="--", marker="."
    )

    # Título e eixos
    plt.title("Funções Seno e Cosseno")
    plt.xlabel("Radianos")
    plt.ylabel("Valor da função")

    plt.xticks(
        [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
        [r"$0$", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"],
    )

    plt.grid(True)
    plt.legend()
    plt.tight_layout()


# 2. Peça ao usuário escolher se a figura deve ser mostrada na tela ou salva em um arquivo.
if __name__ == "__main__":
    plot_sine_cosine()

    choice = input("Digite 'mostrar', 'salvar' ou 'ambos': ").strip().lower()

    if choice in ("salvar", "ambos"):
        filename = input("Digite o nome do arquivo (ex.: grafico.png): ")
        file_path = Path(__file__).resolve().parent.parent / "assets" / filename

        plt.savefig(file_path)
    if choice in ("mostrar", "ambos"):
        plt.show()
    else:
        print("Opção inválida.")
        plt.close()
