def media(numeros):
    return sum(numeros) / len(numeros)

numeros = []

while True:
    print(f'{'='*10} MÉDIA ENTRE OS NÚMEROS {'='*10}')
    print('1 - Adicionar números,')
    print('2 - Calcular a média entre os números.')

    opcao = int(input('Informe a opção desejada: '))

    match opcao:
        case 1:
            novo_num = int(input('Informe o número a ser adicionado: '))
            numeros.append(novo_num)
            print(f'Número {novo_num} adicionado com sucesso.')
        case 2:
            print(f'Média da lista: {media(numeros)}')
