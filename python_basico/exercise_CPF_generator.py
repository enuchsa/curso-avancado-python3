"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re
# CPF = '746.824.890-70'
CPF = re.sub(
    r'[^0-9]',
    '',
    '746.824.890-70'
)
nove_digitos = CPF[:9]
regret_count = 10
result = 0

primeiro_caracter = 'aaaaa'
primeiro_caracter_repetido = primeiro_caracter[0] * len(primeiro_caracter)
if primeiro_caracter == primeiro_caracter_repetido:
    print('cpf invalido')

for digito in nove_digitos:
    result += int(digito) * regret_count
    regret_count -= 1
    
digito_1 = (result * 10) % 11
digito_1 = 0 if digito_1 > 9 else digito_1

dez_digitos = CPF[:10]
regret_count = 11
result = 0
for digito in dez_digitos:
    result += int(digito) * regret_count
    regret_count -= 1

digito_2 = (result * 10) % 11
digito_2 = 0 if digito_2 > 9 else digito_2

new_cpf = f'{nove_digitos}{digito_1}{digito_2}'

if new_cpf == CPF:
    print('Valido!')