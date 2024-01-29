qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    print('-' * 5)
    while coluna <= qtd_colunas:
        print(f'Linha: {linha} - Coluna: {coluna}')
        coluna += 1
    
    linha +=1
    
print('Acabou')