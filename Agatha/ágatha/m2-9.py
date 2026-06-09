# 9 Calculadora Simples
while True:
    print("\n1- Somar\n2- Subtrair\n3- Multiplicar\n4- Dividir\n5- Sair")
    opcao = input("Escolha: ")
    if opcao == "5":
        break
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", a + b)
    elif opcao == "2":
        print("Resultado:", a - b)
    elif opcao == "3":
        print("Resultado:", a * b)
    elif opcao == "4":
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("Erro: divisão por zero!")
