# 11. Média com WHILE
soma, qtd = 0, 0
while True:
    num = int(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    soma += num
    qtd += 1
if qtd > 0:
    print("Média:", soma/qtd)
else:
    print("Nenhum número inserido.")

