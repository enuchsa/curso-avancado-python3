"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

text = iter('luiz') # __iter__

print(next(text))

while True:
    try:
        letra = next(text)
        print(letra)
    except StopIteration:
        break