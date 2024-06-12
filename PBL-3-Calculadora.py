while True:
    print('----| Menu Calculadora |----\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n0 - Sair')
    op = int(input('Digite sua opção: '))
    if op != 0:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        if op == 1:
            print(f'{n1} + {n2} = {n1+n2}')
        if op == 2:
            print(f'{n1} - {n2} = {n1-n2}')
        if op == 3:
            print(f'{n1} * {n2} = {n1*n2}')
        if op == 4:
            print(f'{n1} / {n2} = {n1/n2}')
    else:
        print('Encerrando a calculadora...')
        break
