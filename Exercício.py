salario_hora = float(input('Informe o salário hora:'))
horas = int(input('Informe o número de horas trabalhadas:'))

salario_bruto = salario_hora * horas

salario_inss = salario_bruto * 0.08
salario_ir = salario_bruto * 0.11
salario_sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (salario_ir + salario_sindicato + salario_inss)

print('O salário bruto é: R$', salario_bruto)
print('O desconto do INSS é R$:',salario_inss)
print('O pagamento ao sindicato é:R$', salario_sindicato)
print('O salário líquido é:R$', salario_liquido)