# Defina os custos e o lucro por lanche
custo_lanche = 5.50 + 1.50 + 0.85 + 1.20  # Custo total de ingredientes por lanche
preco_lanche = 15.50  # Preço de venda de cada lanche

# Solicite o valor desejado de lucro por mês do usuário
lucro_desejado = float(input('Digite quanto deseja lucrar por mês: '))

# Valide a entrada do usuário
if lucro_desejado <= 0:
    print('Por favor, digite um valor de lucro mensal válido e positivo.')
else:
    # Calcule quantos lanches você precisa vender diariamente para atingir o objetivo de lucro mensal
    lucro_mensal = lucro_desejado / 30  # Lucro desejado por dia
    lanches_diarios = lucro_mensal / (preco_lanche - custo_lanche)  # Lanches necessários por dia

    print(f'Para atingir um lucro mensal de R${lucro_desejado:.2f}, você precisa vender aproximadamente {round(lanches_diarios)} lanches por dia.')

