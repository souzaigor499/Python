# ex005
palavra = input('Digite uma frase ')
def vogais(string):
  
  string = string.replace('A','*').replace('E','*').replace('I','*').replace('O','*').replace('U','*').replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*')
  return string
frase = vogais(palavra)
print(frase)  