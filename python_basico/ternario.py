"""
Operação ternária em python
"""
condicao = 10 == 11
variavel = condicao if condicao else 'deu errado'
# print('valor' if True else 'outro valor')
print(variavel)

digito = 9
novo_digito = digito if digito >= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)