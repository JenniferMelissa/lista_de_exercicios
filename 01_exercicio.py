try:
    numero = float(input('Informe um número: '))

    print(numero)
    print(type(numero))
except Exception as e:
    print('Não foi possível realizar a operação.')