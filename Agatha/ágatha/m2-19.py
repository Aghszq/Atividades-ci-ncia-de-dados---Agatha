# 19 jogo da forca simplificado 
palavra = "python"
tentativas = 6
acertos = ["_"] * len(palavra)

while tentativas > 0 and "_" in acertos:
    print(" ".join(acertos))
    letra = input("Digite uma letra: ").lower()
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                acertos[i] = letra
    else:
        tentativas -= 1
        print("Errou! Tentativas restantes:", tentativas)

if "_" not in acertos:
    print("Parabéns, você venceu!")
else:
    print("Você perdeu! A palavra era:", palavra)

