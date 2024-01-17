"""
Exercício:
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e dade forem digitados:
    exiba:
        seu nome é:
        seu nome invertido é:
        seu nome contém (ou não) espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é:
        a última letra do seu nome é:
        se nada for digitado em nome ou idade:
        exiba "Desculpe, você deixou campos vazios."
"""

name = input("Digite seu nome: ")
age = input("Digite sua idade: ")

if age.isdigit():
    age = int(age)
    
if name == '' and age == '':
    print("Desculpe, você deixou campos vazios.")
else:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')
    print(f'Seu nome contém espaços?: {' ' in name}')
    print(f"A primeira letra do seu nome é {name[0]}")
    print(f"A última letra do seu nome é {name[len(name) - 1]}")