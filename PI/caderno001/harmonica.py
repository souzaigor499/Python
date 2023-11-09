nums = input('Digite cinco npumeros eparados por espaço ')

nums_str = nums.split()
arr = []
for el in nums_str:
      arr.append(float(el))

def harmonica(arr_nums):

  print(arr_nums)
  indice = 0
  contador = 0
  num_elem = len(arr_nums)
  soma = 0
  elem = 0

  if num_elem != 5:
    return 'Digite cinco números'

  while contador < num_elem:
    elem = 1 / arr_nums[indice]
    print(elem)
    soma = soma + elem
    indice = indice + 1
    contador = contador + 1
  soma = (soma ** -1 ) * num_elem
  return soma

ans = harmonica(arr)
print(ans)