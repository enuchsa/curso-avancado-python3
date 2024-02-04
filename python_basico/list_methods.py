lista = [1, 2, 3, 4, 5]

lista[2] = 10

print(lista)
print(lista[2])

del lista [2] # deletando o valor do indice 2

print(lista)

lista.append(50)

print(lista)
removido = lista.pop()
print(removido)

lista.insert(2, "sexo") # inserindo um dado pelo indice
print(lista)