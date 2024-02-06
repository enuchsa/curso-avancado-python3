"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo o seu código.
Elas podem receber vários valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

def hello(name='Sem nome'):
    print(f'Olá, {name}!')
    
hello()
hello("Enuch")
hello("Natália")
