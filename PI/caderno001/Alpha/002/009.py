# ex009
arqsaida = open('teste.txt', 'w')
txt = input("digite o texto para salvar no arquivo ")
txt2 = input("digite o texto para salvar no arquivo ")
txt3 = input("digite o texto para salvar no arquivo ")
# grava conteúdo no arquivo
arqsaida.write(txt)
arqsaida.write('\n')
arqsaida.write(txt2)
arqsaida.write('\n')
arqsaida.write(txt3)

arqsaida.close()

