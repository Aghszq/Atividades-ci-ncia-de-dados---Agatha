# 3 Senha com Tentativas
senha_correta = "1234"
tentativas = 3
while tentativas > 0:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado!")
        break
    else:
        tentativas -= 1
        print("Senha incorreta. Tentativas restantes:", tentativas)
if tentativas == 0:
    print("Bloqueado!")
