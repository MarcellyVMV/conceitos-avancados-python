def fuel():
    while True:
        fraction = input("\nFração: ")
        try:
            x, y = map(int, fraction.split('/'))
            if y <= 0:
                raise ZeroDivisionError("Y não pode ser zero ou negativo")
            if x > y or x < 0:
                raise ValueError("X não pode ser maior que Y ou negativo")
        except (ZeroDivisionError, ValueError) as e:
            print(f"Erro: {e}. Tente novamente.")
        else:
            percentage = round((x / y) * 100)
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return str(percentage) + "%"
            
print(fuel())