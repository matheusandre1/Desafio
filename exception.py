while True:
        try:

            nome = str(input("Digite seu nome: "))
            ano = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                print(nome)
                print(ano);
            else:
                print("Ano inválido. Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

