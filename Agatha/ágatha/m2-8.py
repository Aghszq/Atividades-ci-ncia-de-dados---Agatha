# 8 Verificador de Primo
num = int(input("Digite um número: "))
eh_primo = True
if num < 2:
    eh_primo = False
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            eh_primo = False
            break
print("É primo?" , eh_primo)
