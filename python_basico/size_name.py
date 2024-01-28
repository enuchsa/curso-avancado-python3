"""
Faça um programa que peça ao usuári o seu nome e se tiver menos de 4 letras
diga que seu nome é curto, se tiver entre 5 e 6 letras é normal e se for maior
que 6 letras é grande
"""

name = input("Digite seu nome: ")

if len(name) <= 4:
    print("Seu nome é curto demais trouxa!")

if 5 <= len(name) <= 6:
    print("Seu nome é normal demais bobão!")
    
if len(name) > 6:
    print("Seu nome é grande demais seu otário!")