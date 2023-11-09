# ex005
nome = input('Me diga seu nome ')
salario = float(input('Digite seu salário '))
vendas = float(input('Digite quanto fez em vendas '))
vendas = vendas * 0.05
salario = salario + vendas
texto_salario = f'{salario:_.2f}'
texto_salario = texto_salario.replace('.',',').replace('_','.')
print(f'Você irá receber R$ {texto_salario} no final do mês')