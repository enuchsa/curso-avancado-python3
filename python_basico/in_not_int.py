# Operadores in e not in
# Strings são iteraveis

# 0 1 2 3 4
# E n u c h
#-5-4-3-2-1

name = 'Enuch'
# print(name[2]) # indice positivo
# print(name[-3]) # indice negativo

# print('u' in name) # verifica se 'u' está em name
# print('Enu' in name)
# print('enu' in name)
# print('enu' not in name)

name_2 = input('Type your first name: ')
find = input('Type what you want to find: ')

if find in name_2:
    print(f'{find} is in {name_2}')
else:
    print(f'{find} is not in {name}')