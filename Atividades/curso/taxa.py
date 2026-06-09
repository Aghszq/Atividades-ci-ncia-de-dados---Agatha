#Declarar uma constante(sempre letra maiuscula)

TAXA_DE_JUROS = 5.12

valor_us = 100
valor_br = valor_us * TAXA_DE_JUROS

#o f" serve pra colocar váriaveis no texto, nesse caso aqui, a variável vai ser o valor em dólar
print(f"US$ {valor_us} = R$ {valor_br:.2f}") #o :2.f formata os números decimais 

