#mportar biblioteca
from datetime import date 

evento = []
classificacao = []


data = f'{date.today().day}/{date.today().month}/{date.today().year}'

while True:
    print(f'{'='*10} EVENTOS {'='*10}')
    print('1 - Cadastrar novo evento.')
    print('2 - Lista de eventos.')
    print('3 - Participar de algum evento.')
    print('4 - Sair do programa.')

    opcao = int(input('Informe opção desejada: '))

    try:
        match opcao:
            case 1:
                nome_evento =input('Informe o nome do evento: ')
                evento.append(nome_evento)
                nova_classificacao = input('Informe classificação do filme: ')
                classificacao.append(nova_classificacao)
                print(f'Evento: {nome_evento} Classificação: {nova_classificacao}')
                continue
            case 2:
                    for evt, clsf in zip(evento, classificacao):
                        print(f'Evento: {evt} - Classificação: {clsf}')
                        continue
            case 3:
                nome = input('Informe seu seu nome: ')
                idade = int(input('Informe sua idade: '))

                evento_escolhido = input('Informe o evento desejado: ')

                if evento_escolhido in evento:
                    indice_evento = evento.index(evento_escolhido)
                    classif_evento = classificacao[indice_evento]


                    if idade >= int(classif_evento):
                        print('\n')
                        print(f'Ingresso impresso no dia: {data}')
                        print(f'Pagante: {nome}.')
                        print(f'Evento: {evento_escolhido}.')
                        break
                    else:
                        print(f'{nome} não possui a idade mínima para participar do evento: {evento_escolhido}.')
                        print('Favor, escolher outro evento.')
                        continue
                else:
                    print(f'O evento {evento_escolhido} não foi encontrado.')
                    continue
            case 4:
                print('Programa encerrado.')
                break
    except:
        print('Opção informada não é valida.')
                





# #incio do loop
# while True: 
#     print(f'{'='*30} LISTA DE FILMES {'='*30}')
#     print(f'{data}\n')
#     print('1 - KIMETSU NO YAIBA - 16 anos')
#     print('2 - NARUTO - 12 anos')
#     print('3 - KIMI NO NA WA - 14 anos')
#     print('4 - SHINGEKI NO KYOJIN - 16 anos')
#     print('5 - SPY X FAMILY - 10 anos')
#     print('6 - Turma da Mônica - Livre')

#     #escolha do usuario 
#     sala = input('\nSala desejada: ')

#     #limpar console
#     os.system('cls')

#     #inicio do loop
#     match sala:
#         case '1':
#             idade_minima = 16
#             filme = 'KIMETSU NO YAIBA'
#         case '2':
#             idade_minima = 12
#             filme = 'NARUTO'
#         case '3':
#             idade_minima = 14
#             filme = 'KIMI NO NA WA'
#         case '4':
#             idade_minima = 16
#             filme = 'SHINGEKI NO KYOJIN'
#         case '5':
#             idade_minima = 10
#             filme = 'SPY X FAMILY'
#         case '6':
#             idade_minima = 0
#             filme = 'Turma da Mônica'
#         case _:
#             print('Sala inexistente. Favor, escolher outra sala.')
#             continue
#     #verficacao da idade
#     if idade >= idade_minima:
#         print(f'Ingresso impresso no dia: {data}\n')
#         print(f'Pagante: {nome}.')
#         print(f'Filme: {filme}.')
#         print(f'Sala: {sala}.')
#         print(f'Tenha um ótimo filme!')
#         break
#     else:
#         print(f'{nome} não possui a idade mínima para o filme {filme}.')
#         print('Favor, escolher outro filme.')
#         continue