count = 0
count_pares = 0

while True:
    num = int(input("Digite um número positivo (ou um número negativo para sair): "))
    if num < 0:
        break
    count += 1
    if num % 2 == 0:
        count_pares += 1

if count == 0:
    print("Nenhum número positivo foi digitado.")
else:
    percent_pares = (count_pares / count) * 100
    print(f"A porcentagem de números pares digitados é de {percent_pares:.2f}%")
