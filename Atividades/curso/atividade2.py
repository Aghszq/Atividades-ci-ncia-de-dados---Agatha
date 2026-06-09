reais = float(input("Digite o valor em reais: "))
cotacao = float(input("Digite a cotação do dólar: "))
dolares = reais / cotacao

print(f"Valor em dólar: US$ {dolares:.2f}")