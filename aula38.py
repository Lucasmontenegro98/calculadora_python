while True:
    numero_1 = input('digite um numero: ')
    numero_2 = input('digite outro numero: ')
    operador = input('digite o operador (+,-,*,/): ')
    
    numeros_validos = None
    num_1_float = 0 #transformar em float
    num_2_float = 0 #transformar em float
    try:
        num_1_float = float(numero_1) #transformar em float
        num_2_float = float(numero_2) #transformar em float

        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('um ou ambos numeros sao invalidos')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('esse operador nao é permitido')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue
    
    #aplicar as operações

    if operador == '+':
        print(num_1_float + num_2_float)

    elif operador == '-':
        print(num_1_float - num_2_float)

    elif operador == '*':
        print(num_1_float * num_2_float)

    elif operador == '/':
        print(num_1_float / num_2_float)
    
    sair = input('quer sair? [s]im: ')
    
   
    if sair[0] == 's':
        print('vc saiu do sistema') 
    
        break
   