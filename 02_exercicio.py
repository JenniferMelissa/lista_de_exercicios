peso = input('Informe o peso em gramas do recém-nascido: ').replace(',','.')
peso_float = float(peso)


if peso_float < 2500:
    print('Está abaixo do peso. O recém-nascido precisará ficar internado.')

else:
    print('O recém nascido está com o peso normal. Está liberado para ir para casa.')