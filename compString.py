str1 = input('Informe a primeira string:')
str2 = input('Informe a segunda string:')

print(f'A primeira string é {str1}, e seu comprimento é {len(str1)}')
print(f'A primeira string é {str2}, e seu comprimento é {len(str2)}')

if len(str1) == len(str2):
    print('As duas strings são do mesmo tamanho')
else:
    print('As duas strings são de tamanhos diferentes')

if str1 == str2:
    print('As duas strings possuem o mesmo conteúdo')
else:
    print('As duas strings são diferentes')
    