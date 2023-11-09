nome = input('Digite seu nome completo ')
email = nome[0:nome.find(' ')] + '.' + nome[nome.find(' ') + 1 :]
email = email[0:email.find(' ')] + '@gmail.com'
print(email)