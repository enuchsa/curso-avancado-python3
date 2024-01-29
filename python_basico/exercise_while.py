
name = 'Enuch Santos'
count = 0
new_string = '*'


while count < len(name):
    new_string += name[count] + '*'
    count += 1
    
print(new_string)