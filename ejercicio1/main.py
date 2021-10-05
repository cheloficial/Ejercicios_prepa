print('Bienvenido a mi calculadora!\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Potencia\n6. Modulo\n7. Comparar\n8 Valor absoluto')

s = input('Ingrese el numero correspondiente a su seleccion: ')

if s.isnumeric():
   
   if int(s) in range(1,9): 
    
        x = float(input('Ingrese el primer numero: '))
    
        if int(s) in range(1, 8):
            y = float(input('Ingrese el segundo numero: '))
            s = int(s)
    
            if s == 1:
                print(f'{x} + {y} = {x+y}')
            elif s == 2:
                print(f'{x} - {y} = {x-y}')
            elif s == 3:
                print(f'{x} * {y} = {x*y}')
            elif s == 4:
                if y == 0:
                    print('La division entre 0 no esta definida.')
                else:
                    print(f'{x} / {y} = {x/y}')               
            elif s == 5:
                print(f'{x} ^ {y} = {x**y}')
            elif s == 6:
                print(f'{x} % {y} = {x%y}')
            elif s == 7:
                if x > y:
                    print(f'{x} > {y}')
                elif y > x:
                    print(f'{y} > {x}')
                else:
                    print(f'{x} = {y}')       
        elif int(s) == 8:
            if x < 0:
                print(f'El valor absoluto de {x} es {-x}')
            else:
                print(f'El valor absoluto de {x} es {x}')
   else:
       print('El numero ingresado no corresponde a ninguna operacion')    
else:
    print('Ingreso invalido.')    