import random

print('PEDRA, PAPEL OU TESOURA')
print('Digite um número para fazer sua escolha:')
print('1 - PEDRA')
print('2 - PAPEL')
print('3 - TESOURA')

x = int(input('Faça sua escolha '))
y = random.randint(1, 3)

if y == 1:
  escolhaBot = 'PEDRA' 
elif y == 2:
  escolhaBot =  'PAPEL'
else:
  escolhaBot = 'TESOURA'

if x > 3 or x < 1:
  print('Valor Invalido')
else:
  if x == 1:
    escolha = 'PEDRA' 
  elif x == 2:
    escolha =  'PAPEL'
  elif x == 3:
    escolha = 'TESOURA'
  if escolha == escolhaBot:
   print(escolha, 'contra', escolhaBot, '\nEMPATE')
  elif (escolha == 'PEDRA' and escolhaBot == 'TESOURA') or (escolha == 'PAPEL' and escolhaBot == 'PEDRA')  or (escolha == 'TESOURA' and escolhaBot == 'PAPEL'):
    print(escolha, 'contra', escolhaBot, '\nVocê venceu!')
  else:
    print(escolha, 'contra', escolhaBot, '\nVocê perdeu :(')
