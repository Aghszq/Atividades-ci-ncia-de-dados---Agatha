# 15 Soma Dígitos com FOR
num = input("Digite um número: ")
soma = 0
for digito in num:
    soma += int(digito)
print("Soma dos dígitos:", soma)

