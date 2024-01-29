""" Calculadora com while """

while True:
    num_1 = input('Type a number: ')
    num_2 = input('Type another number: ')
    operator = input('Type a operator [+ - * /]: ')
    result = ...
    
    num_float_1 = 0.0
    num_float_2 = 0.0
    
    valid_operators = '+-*/'
    
    if len(operator) > 1:
        print('Just one operator')
        continue
    
    if operator not in valid_operators:
        print("It's not a valid operator!")
        continue
    
    try:
        num_float_1 = float(num_1)
        num_float_2 = float(num_2)
    except:
        print("It's not a valid number!")
        
    if operator == '+':
        result = num_float_1 + num_float_2
    elif operator == '-':
        result = num_float_1 - num_float_2
    elif operator == '*':
        result = num_float_1 * num_float_2
    elif operator == '/':
        result = num_float_1 / num_float_2
                
    print(f'{num_float_1} {operator} {num_float_2} = ? \
            \nresult: {result}')
        
    leave = input('Exit? [s]im: ').lower().startswith('s')
    
    if leave:
        break
    
    
    
    