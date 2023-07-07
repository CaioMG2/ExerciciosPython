peso = float(input('Informe o peso do peixe:'))
excesso = 0
multa = 0

if peso <= 50:
    print('Excesso:', excesso)
    print('Multa:', multa)
else:
    excesso = peso - 50
    multa = excesso * 4

    print('Excesso:', excesso)
    print('Multa:,', multa)
