area = int(input('Informe a área em m²:'))

litros = (area / 3)
latas = int(litros / 18)

if litros % 18 != 0:
    latas += 1

print('Você deve comprar', latas, 'latas')
print('O valor total é:,' (latas * 80))

