def media():
    sum(numeros) /len(numeros)
    return media

numeros = []

while True:
    print(f'{'='*10} MÉDIA ENTRE OS NÚMEROS {'='*10}')
    print('1 - Adicionar números,')
    print('2 - calcular a média entre os números.')
    
    opcao = int(input('informe opção desejada: '))

    match opcao:
        case 1:
            novo_num = int(input('Informe número a ser adicionado: '))
            numeros.append()
            print(f'Número {novo_num} adicionado com sucesso.')
        case 2:
            print(f'Média da lista: {media}')
            
    

    