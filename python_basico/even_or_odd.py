# Faça um algoritmo que receba um número inteiro e informe se este número é
# par ou ímpar, caso não seja informado um número inteiro informe ao usuário
# que não é um númeiro inteiro

num = input('Digite um número inteiro: ')

if num.isnumeric():
    num = int(num)
    
    if num % 2 == 0:
        print("É par")
    else:
        print("É ímpar")
else:
    print("Não foi digitado um número inteiro")


    
