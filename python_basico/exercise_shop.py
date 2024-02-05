"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidad de inserir, pagar e listat valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista
"""
cart = []
while True:
    action = input(f'Selecione uma opção \
        \n[i]nserir [a]pagar [l]istar:')
    
    if len(action) > 1 or action not in 'ial':
        print('Digite apenas as opção mostradas')
        continue
    
    if action == 'i':
        item = input(f'Digite o item que deseja adicionar: ')
        cart.append(item)
    elif action == 'a':
        index = input(f'Digite o índice do item que deseja apagar: ')
        if not index.isdigit():
            continue
        index = int(index)
        if not (index <= len(cart) - 1):
            continue
        del cart[index]
    elif action == 'l':
        for index, name in enumerate(cart):
            print(index, name)