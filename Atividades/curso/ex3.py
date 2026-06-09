dia_semana = int(input("Digite o dia da semana (1-7): "))
data = input("Digite a data (dd/mm): ")

if dia_semana >= 2 and dia_semana <= 6 and data != "25/12":
    print("É um dia útil.")
else:
    print("Não é um dia útil.")