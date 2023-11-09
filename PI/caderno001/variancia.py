nums = input('Digite cinco números separados por espaço ')

nums_str = nums.split()
arr = []
for el in nums_str:
    arr.append(float(el))


def mediaVariancia(arr_nums):

# σ² = ( (Σ x²) / N ) - μ²
  indice = 0
  contador = 0
  num_elem = len(arr_nums)
  soma = 0
  somaq = 0

  if num_elem != 5:
    return 'Digite cinco números'


  while contador < num_elem:
    soma = soma + arr_nums[indice]
    somaq = somaq + arr_nums[indice] ** 2
    indice = indice + 1
    contador = contador + 1

  media = soma / num_elem
  mediaq = somaq / num_elem
  variancia = mediaq - (media * media)
  resp = 'Média:' , media, 'Variância :', variancia
  return resp

ans = mediaVariancia(arr)

print(ans)