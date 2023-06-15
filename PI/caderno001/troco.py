troco = int(input('Digite o valor do troco '))

cinque = troco // 50
troco = troco % 50
vinteCin = troco // 25
troco = troco % 25
dez = troco // 10
troco = troco % 10
cinco = troco // 5
troco = troco % 5
um = troco 

print(cinque, 'moeda(s) de 50 centavos.')
print(vinteCin, 'moeda(s) de 25 centavos.')
print(dez, 'moeda(s) de 10 centavos.')
print(cinco, 'moeda(s) de 5 centavos.')
print(um, 'moeda(s) de 1 centavo.')
