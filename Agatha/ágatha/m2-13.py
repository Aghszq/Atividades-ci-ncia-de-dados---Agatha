# 13 Fatorial com FOR
num = int(input("Digite um número para calcular o fatorial: "))
fat = 1
for i in range(1, num+1):
    fat *= i
print("Fatorial:", fat)

