"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""


x = 1

def scope():
    global x 
    x = 10
    def another_function():
        y = 2
        print(x, y)
        
    another_function()
    print(x)
    
print(x)    
scope()
print(x)    