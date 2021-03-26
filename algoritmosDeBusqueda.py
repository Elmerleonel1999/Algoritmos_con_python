#algoritmo de busqueda lineal
def linearSearch(numberList, objective):
  match = False
  for number in numberList:
      if number == objective:
        match = True
        break
  return match

#algoritmo de busqueda binaria o BinarySearch
def binarySearch(numberList,start, final, objective):
  pass
  

if __name__ == '__main__':
  numeros = range(20)
  
  print(linearSearch([1,5,4,9,7,3], 20))
  print(linearSearch(numeros,15))
  
  
  