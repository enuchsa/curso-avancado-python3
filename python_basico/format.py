a = 'AA'
b = 'BBB'
c = 1.1
# método format com argumentos e um parâmetro
string = 'b={1} a={0} a={0} a={0} c={nome3:.2f}'
formato = string.format(a, b, nome3=c)

# método format com parâmetros
string = 'b={nome2} a={nome1} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)