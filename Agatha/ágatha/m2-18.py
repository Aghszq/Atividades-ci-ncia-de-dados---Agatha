# 18 Contador de Consoantes
texto = input("Digite um texto: ")
vogais = "aeiouAEIOU"
contador = 0
for letra in texto:
    if letra.isalpha() and letra not in vogais:
        contador += 1
print("Quantidade de consoantes:", contador)

