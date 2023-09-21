altura = float(input('Digite sua altura em m: '))
peso = float(input('Digite seu peso em kg: '))
imc = round(peso / (altura ** 2))
if peso and altura >= 0:
    print(f'''Seu IMC é {imc}. O valor ideal considerando peso normal é de: 
Mulheres = 19,1-25,8.
Homens = 20,7-26,4.''')