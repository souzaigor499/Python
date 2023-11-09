# ex009
import math
a = float(input('Digite um ângulo '))
d = float(input('Digite a distância entre as cidades '))

raio = (d * 180) / math.pi / a
c = 2 * math.pi * raio
kilo = (c * 176.4) / 1000
print(f'{c} estádios e {kilo} kilômetros')