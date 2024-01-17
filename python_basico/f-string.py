"""
Formatação básica de strings
s - string
d - int
f - float
. <número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^- Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:0^10}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{1000.43242424:0=+10,.1f}')
# Preenche com 0 os espaços em branco, coloca o + na frente de todos os números, 
# Coloca um ',' em números acima de mil, coloca 10 espaços
