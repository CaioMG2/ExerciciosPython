numero_digitado = input("Digite um número inteiro: ")

# Verifica se a entrada contém apenas dígitos (números inteiros)
if numero_digitado.isdigit():
    numero = int(numero_digitado)
    if numero % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} é um número ímpar.")
else:
    try:
        numero_float = float(numero_digitado)
        if numero_float.is_integer():
            numero = int(numero_float)
            if numero % 2 == 0:
                print(f"{numero} é um número par.")
            else:
                print(f"{numero} é um número ímpar.")
        else:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    except:
        print("Entrada inválida. Por favor, digite um número inteiro.")
