# ex010
num = int(input('Digite um número de 4 dígitos '))

quarto = num // 10
quarto = quarto * 10
quartofinal = num - quarto
terceiro = num // 100
quarto = quarto / 10
terceiro = terceiro * 10
terceirofinal = int(quarto - terceiro)
segundo = num // 100
segundo = segundo - ((num // 1000) * 10)
primeiro = num // 1000
quartofinal += 1
quartofinal = quartofinal % 10
terceirofinal +=1
terceirofinal = terceirofinal % 10
segundo += 1
segundo = segundo % 10
primeiro +=1
primeiro = primeiro % 10

print(primeiro, segundo, terceirofinal, quartofinal, sep='')