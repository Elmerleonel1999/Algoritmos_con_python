#algoritmo de busqueda lineal
def linearSearch(numberList, objective):
  match = False
  for number in numberList:
      if number == objective:
        match = True
        break
  return match

#algoritmo de busqueda binaria o BinarySearch
def binarySearch(numberList, objective):
  start = numberList[0]
  final = numberList[len(numberList) - 1]
  
  while start <= final:
    if start == objective:
      return 1
    
    if objective == 0:
      print("no se admite el => [ 0 ] ")
      return False
    
    half = (start + final) // 2
    if numberList[half] == objective:
      return True
    
    if numberList[half] > objective:
      final = half
      half = (start + final) // 2
      
    if numberList[half] < objective:
      start = half
      half = (start + final) // 2
      
  else:
    return False

if __name__ == '__main__':
  numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  
  result = binarySearch(numeros, 0)
  print(result)
  
  
  
  
  
  
  
  
  