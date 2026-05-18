def read_input(n1, n2):
    while True:
        try:
            number = int(input(f"\nPor favor entre com um número: "))
            if number < n1 or number > n2:
                raise ValueError
        except ValueError:
            print(f"Você deve entrar com um número inteiro entre {n1} e {n2}")
        else:
            return number
        
print(f"Você digitou {read_input(5, 10)}")