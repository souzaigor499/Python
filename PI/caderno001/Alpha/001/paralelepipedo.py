# ex002
import math
a = float(input('Digite um lado do paralelepípedo '))
b = float(input('Digite outro lado do paralelepípedo '))
c = float(input('Digite o último lado do paralelepípedo '))
volume = a * b * c
diagonal = math.sqrt(a*a + b*b + c*c)
print(f'Volume: {volume:.2f} Diagonal: {diagonal:.2f}')