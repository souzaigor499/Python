

ref_arquivo = open('teste.txt', 'r')


for linha in ref_arquivo:
  print(linha)
ref_arquivo.close
# Sempre é necessário fechar o arquivo após modificação para evitar erros no arquivo
