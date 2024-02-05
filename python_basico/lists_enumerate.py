"""
enumerate - enumera iteráveis (índices)
"""

lista = ['maria', 'lucas']
lista.append('loana')

lista_enumerada = enumerate(lista)
lista_enumerada = list(enumerate(lista))

# for item in lista_enumerada:
#     indice, nome = item
#     print(indice, nome)
    
for indice, nome in lista_enumerada:
    print(indice, nome)
    
# Após ler todos os items do enumerate eles não aparecem mais