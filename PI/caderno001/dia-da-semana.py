dia = int(input('Digite o dia '))
mes = int(input('Digite o mês '))
ano = int(input('Digite o ano '))

a0 = ano - (14 - mes) // 12
x = a0 + a0 // 4 - a0 // 100 + a0 // 400
m0 = mes + 12 * ((14 - mes) // 12) - 2
d0 = (dia + x + (31 * m0)//12) % 7


print(d0)