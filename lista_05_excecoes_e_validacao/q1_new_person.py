def new_person():
    while True:
        try:
            name = input("\nNome: ")
            if not name or len(name.split()) < 2 or len(name) > 40:
                raise ValueError("Nome invalido, o nome deve ter pelo menos duas palavras e no máximo 40 caracteres")
            age = int(input("Idade: "))
            if age < 0 or age > 150:
                raise ValueError("Idade invalida, a idade deve ser um inteiro entre 0 e 150")
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
        else: 
            return (name, age)
 
print(new_person())