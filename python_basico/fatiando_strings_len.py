"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[0:8])
print(variavel[0:9:2]) # Indo de 2 em 2 caracteres
print(variavel[::-2]) # Indo de 2 em 2 caracteres só que invertendo a string
print(len(variavel))