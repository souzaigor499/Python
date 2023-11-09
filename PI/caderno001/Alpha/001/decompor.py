# ex007
valor = int(input('Digite um número inteiro '))

duzentos = valor // 200
valor = valor % 200
cem = valor // 100
valor = valor % 100
cinq = valor // 50
valor = valor % 50
vinte = valor // 20
valor = valor % 20
dez = valor // 10
valor = valor % 10
cinco = valor // 5
valor = valor % 5
dois = valor // 2
valor = valor % 2
um = valor

print('O valor pode ser decomposto em:')
print(f'{duzentos} cédula(s) de R$200,00')
print(f'{cem} cédula(s) de R$100,00')
print(f'{cinq} cédula(s) de R$50,00')
print(f'{vinte} cédula(s) de R$20,00')
print(f'{dez} cédula(s) de R$10,00')
print(f'{cinco} cédula(s) de R$5,00')
print(f'{dois} cédula(s) de R$2,00')
print(f'{um} cédula(s) de R$1,00')
