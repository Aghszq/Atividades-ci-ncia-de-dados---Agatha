# 16  Progressão Aritmética
a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
n = int(input("Quantidade de termos: "))
for i in range(n):
    print(a1 + i*r, end=" ")
print()
