def verificar_impar_par(numero):

    if  numero % 2 == 0:
        return 'Número par.'
    else:
        return 'Número ímpar.'

try:
    informar_numero = int(input('Informe o número que deseja verificar: '))
    resultado = verificar_impar_par(informar_numero)
    print(resultado)
except:
    print('Não foi possível verificar o número informado.')

