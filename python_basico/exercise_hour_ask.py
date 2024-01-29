"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.
"""

hour = input("Digite a hora atual: ")

try:
    hour = int(hour)
    
    if 0 <= hour <= 11:
        print("Bom dia!")
    if 12 <= hour <= 17:
        print("Boa tarde!")
    if 18 <= hour <= 23:
        print("boa noite!")
except:
    print("Digite um número seu filho de uma puta")
    