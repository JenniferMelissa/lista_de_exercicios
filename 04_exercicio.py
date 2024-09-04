import os 
import time

try:
    contagem_regressiva = int(input('Informe um número inteiro para começar a   contagem regressiva: '))

    os.system('cls')

    print('\nContagem regressiva: \n')

    while contagem_regressiva >= 0:
        print(f'{contagem_regressiva} ...')
        contagem_regressiva -= 1
except Exception as e:
    print(f'Não foi possível realizar a contagem: {e}.')


