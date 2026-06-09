# 20 Multiplicação Russa
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resultado = 0
while a > 0:
    if a % 2 != 0:
        resultado += b
    a //= 2
    b *= 2
print("Resultado:", resultado)
