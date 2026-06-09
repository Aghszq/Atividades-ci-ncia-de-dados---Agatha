# 6 Fibonacci
n = int(input("Quantos termos da sequência de Fibonacci deseja ver? "))
a, b = 0, 1
contador = 0
while contador < n:
    print(a, end=" ")
    a, b = b, a + b
    contador += 1
print()
