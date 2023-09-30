while True:
    print()
    numero1 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    numero2 = input('Digite outro número: ')

    if not numero1.isnumeric() or not numero2.isnumeric():
        print('Digite um número.')
        continue

    numero1 = int(numero1)
    numero2 = int(numero2)

    if operador == '+':
        print(numero1 + numero2)
    elif operador == '-':
        print(numero1 - numero2)
    elif operador == '*':
        print(numero1 * numero2)
    elif operador == '/':
        print(numero1 / numero2)
    else:
        print('Operador invalido')    