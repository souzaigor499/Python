# ex006
x = int(input('Digite um número inteiro '))
y = int(input('Digite um número inteiro '))
z = int(input('Digite um número inteiro '))

max1 = (x + y) / 2 + abs(y-x) /2
max2 = (max1 + z) / 2 + abs(z - max1) / 2
max2 = int(max2)

print(f'O maior número é o {max2}')