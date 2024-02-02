frase = 'o python é uma linguagem de programação multiparadigma. python foi criado por guido van rossum'

i = 0
letra_apareceu_mais = ''
maior_qtd = 0
qtd_atual = 0
letter = ''
while i < len(frase):
    letra_atual = frase[i]
    
    i = i + 1
    if letra_atual == ' ':
        continue
    
    i_2 = 0
    
    while i_2 < len(frase):
        if letra_atual == frase[i_2]:
            qtd_atual = qtd_atual + 1
        i_2 = i_2 + 1
    
            
    if qtd_atual > maior_qtd:
        maior_qtd = qtd_atual
        letra_apareceu_mais = letra_atual
        
    qtd_atual = 0
    
    
print(maior_qtd, letra_apareceu_mais)