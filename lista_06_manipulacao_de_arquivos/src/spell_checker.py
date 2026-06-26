from pathlib import Path


# 3. Escreva um programa que peça um texto, verifique a ortográfica e exiba o texto com as palavras incorretas entre asteriscos.
def spell_checker(text: str) -> str:
    """
    Verifica ortografia de um texto em inglês, destacando as palavras incorretas com asteriscos.

    Args:
        text (str): Texto a ser verificado.

    Returns:
        str: Texto com palavras verificadas.
    """
    file_path = Path(__file__).resolve().parent.parent / "assets" / "wordlist.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        wordlist = {line.strip().lower() for line in file}
        checked_text = []
        for palavra in text.split():
            # Destaca com asteriscos as palavras que não estão no dicionário.
            if palavra.lower() in wordlist:
                checked_text.append(palavra)
            else:
                checked_text.append(f"*{palavra}*")
        return " ".join(checked_text)


if __name__ == "__main__":
    text = input("\nWrite text: ")
    print(spell_checker(text))
