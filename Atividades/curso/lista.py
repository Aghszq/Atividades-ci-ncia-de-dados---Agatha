#lista de compras
lista = [] 

#isso aqui é um comando de looping que é executado infinitamente enquanto a condição for verdadeira, por isso "while true"
while True:
    print("Lista de Compras")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Ver lista")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1": #nosso if aqui serve pra verificar uma condição verdadeira 
        item = input("Digite o item: ")
        lista.append(item)
        print(f"{item} adicionado!")

    elif opcao == "2": #nosso elif é "senão", ele é executado se a condição anterior for falsa 
        item = input("Digite o item para remover: ")
        if item in lista: #o "in" verifica os elementos que estão dentro de alguma coisa, caso aqui é a lista
            lista.remove(item)
            print(f"{item} removido!")
        else:
            print("Item não encontrado.")

    elif opcao == "3": #"senão" for verdade, vai te retornar a mensagem de erro que você definiu "se" for verdade, vai retornar o valor do que pediu
        print("Sua lista de compras:")
        if len(lista) == 0:
            print("Lista vazia.")
        else:
            for i, item in enumerate(lista, start=1): #"for" é usado pra repetir alguma coisa, no caso aqui é o número 1
                print(f"{i}. {item}")

    elif opcao == "4": #o else segue o mesmo conceito, se estiver errado, retorna a mensagem que vc definiu
        print("Saindo")
        break #o break aqui encerra o looping

    else:
        print("Opção inválida, tente novamente.") 
