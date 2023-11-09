# ex001
raio = float(input('Digite o valor do raio '))
area = 3.14159265 * (raio * raio)
texto_area = f'{area:_.4f}'
texto_area = texto_area.replace('.',',').replace('_','.')
# transaformações para decimais brasileiros

print(f'A área é: {texto_area}')