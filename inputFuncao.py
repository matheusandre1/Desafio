def calculadora():
     while True:
        print("\nEscolha a operacao:")
        print("1 - Soma")
        print("2 - Subtracao")
        print("3 - Multiplicacao")
        print("4 - Divisao")
        print("0 - Sair")

        operacao = int(input("Digite o numero da operacao desejada: "))

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))


        if operacao == 0:
            print("Encerrando...")
            break;

        if operacao == 1:
                resultado = num1 + num2
                print(f"{num1} + {num2} = {resultado}")
        elif operacao == 2:
                resultado = num1 - num2
                print(f"{num1} - {num2} = {resultado}")
        elif operacao == 3:
                resultado = num1 * num2
                print(f"{num1} * {num2} = {resultado}")
        elif operacao == 4:
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    resultado = num1 / num2
                    print(f"{num1} / {num2} = {resultado}")
  


calculadora()