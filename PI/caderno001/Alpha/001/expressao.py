# ex004
import math
a = int(input('Digite um número inteiro: '))
b = int(input('Digite um número inteiro: '))
x = int(input('Digite um número: '))
y = int(input('Digite um número: '))

expressao = a + b * x - math.sqrt(b) + ((a + b) / (x - y))
texto_expressao = f'{expressao:_.2f}'
texto_expressao = texto_expressao.replace('.',',').replace('_','.')


print(f'Expressão: {texto_expressao}')