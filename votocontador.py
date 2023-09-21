def calcular_percentual(votos, total_votos):
    return (votos / total_votos) * 100


def exibir_resultados(votos, total_votos):
    opcoes = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
    print('Resultados das votações:')
    print('------------------------')
    for i in range(len(opcoes)):
        percentual = calcular_percentual(votos[i], total_votos)
        print(f'{opcoes[i]}: {percentual:.2f}%')


votos = [0, 0, 0, 0, 0, 0]

while True:
    print('Escolha o sistema operacional para votar:')
    print('1- Windows Server')
    print('2- Unix')
    print('3- Linux')
    print('4- Netware')
    print('5- Mac OS')
    print('6- Outro')
    print('0- Encerrar votação')
    
    voto = int(input('Digite o número da opção desejada: '))
    
    if voto == 0:
        break
    
    if voto < 0 or voto > 6:
        print('Opção inválida. Por favor, escolha uma opção válida.')
    else:
        votos[voto - 1] += 1

total_votos = sum(votos)

exibir_resultados(votos, total_votos)
