# 7 Lista de Compras
compras = []
while True:
    item = input("Digite um item (ou 'sair' para encerrar): ")
    if item.lower() == "sair":
        break
    compras.append(item)
print("Lista de compras:")
for i in compras:
    print("-", i)
