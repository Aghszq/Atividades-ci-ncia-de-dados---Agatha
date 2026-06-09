#verificação de renda e idade 
idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda: "))

if idade >= 21 and renda > 2000:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")