try:
    peso = int(input('Informe o peso em gramas do recém-nascido: ').replace(',','.'))

    #operador ternario
    print('O bebê está liverado.' if peso >= 2500 else 'O bebê precisa ser internado.')
except Exception as e:
    print(f'Não foi possível calcular o peso do bebê: {e}.')