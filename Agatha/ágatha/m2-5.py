# 5 Adivinhação
import random
numero = random.randint(1, 10)
palpite = 0
while palpite != numero:
    palpite = int(input("Adivinhe o número (1-10): "))
    if palpite < numero:
        print("Muito baixo!")
    elif palpite > numero:
        print("Muito alto!")
print("Parabéns! Você acertou.")
