nome = str(input("Digite seu nome: "))
while True:
        try:

            
            ano = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if ano < 1922 or ano > 2021:
                print("Ano inválido. Por favor, digite um ano entre 1922 e 2021.")
                
            else:
                print(f"{nome}, tem {2024-ano}")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

