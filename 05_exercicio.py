nomes = ['Maria', 'João', 'Julio', 'Ricardo', 'Mariano', 'Cristina', 'Fernanda', 'Rustenio', 'Cleton', 'Roberta']


while True:
    print(f'{'='*10}Lista de Nomes{'='*10}')
    print('1 - Adicionar nomes na lista.')
    print('2 - Exibir a lista.')
    print('3 - Sair do programa.')

    opcao = input('Informe opção desejada: ')

    try:
        match opcao:
            case '1':
                novo_nome = input('Informe nome a ser adicionado: ')
                nomes.append(novo_nome)
                print('Novo nome adicionado com sucesso.\n')
                continue
            case '2':
                for i in range(len(nomes)):
                    print(f'Índice: {i}: {nomes[i]}.\n')
                continue
            case '3':
                print('Programa encerrado.\n')
                break
            case _:
                print('Opção não encontrada.\n')
                continue
    except:
        print('Indíce não encontrado.')
        continue



#     nomes = ['Maria', 'João', 'Julio', 'Ricardo', 'Mariano', 'Cristina', 'Fernanda', 'Rustenio', 'Cleton', 'Roberta']

# try:
#     numero_informado = int(input('Informe um número inteiro índice: '))
#     if 0 <= numero_informado < len(nomes):
#         print(f'{nomes[numero_informado]} encontrada no índice {numero_informado}.')
#     else:
#         print('Índice fora dos limites da lista.')
# except ValueError:
#     print('Por favor, insira um número inteiro válido.')

