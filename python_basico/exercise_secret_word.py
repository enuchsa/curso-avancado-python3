"""
Faça um jogo para o usuário adivihar qual a palavra secreta.
- Vocçe vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário
digitar uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra está na palavra.
    - se a letra estiver na palavra exiba a palavra, se não exiba *
Conte as tentativas
"""

import os


secret_word = 'Evolução'
hits = 0
show_secret_word = '' * len(secret_word)
hit_letters = []
while True:
    hits += 1
    
    print(show_secret_word)
    letter_user = input('Type a single letter or a word complete: ')
    hit_letters.append(letter_user)
    
        
    if len(letter_user) != len(secret_word) and len(letter_user) > 1:
        letter_user = input('Type a single letter or a word complete: ')
      
    if letter_user == secret_word:
        print(f"You win! the word is {letter_user}")
        break
         
    show_secret_word = ''
    count = 0
    hitou = False
    for letter in secret_word:
        if letter in hit_letters:
            show_secret_word += letter
            hitou = True
        else:
            show_secret_word += '*'
        count += 1
        
    if '*' not in show_secret_word:
        print(f"You win! the word is {secret_word}")
        hitou = False
        break
        
        
    if hitou:
        print(f'hits: {hits}')
        print('Nice!')
        print(show_secret_word)
        
        
        
        

