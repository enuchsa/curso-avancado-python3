"""
Argumentos nomeados e não em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y):
    # Definição
    print(f'{x=} {y=} | x + y = {x+y}')
    
soma(1, 2) # Argumentos não nomeados
soma(y=2, x=1) # Argumentos nomeados