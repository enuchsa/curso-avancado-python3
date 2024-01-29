"""
Repetições
While = enquanto
"""

condition = True
count = 1
while condition:
    print(f"Estou em um loop {count}")
    count += 1
    
    if count == 5:
        condition = False
    