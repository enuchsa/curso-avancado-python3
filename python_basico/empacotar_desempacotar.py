nome1, nome2, nome3 = ['Enuch', 'Natália', 'Luana']
print(nome2)

nome1, *resto = ['Enuch', 'Natália', 'Luana']
print(nome1, resto)

_, nome1, *_ = ['Enuch', 'Natália', 'Luana']
print(nome1, _)