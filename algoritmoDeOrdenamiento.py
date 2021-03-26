#ORDENAMIENTO LINEAL

mi_arreglo = [12,4,56,78,1,0,98,25,1,4]
  
def ordenamiento_lineal(lista_numerica):
  aux = 0
  for i in range(0, len(lista_numerica) - 1):
    for j in range(0, len(lista_numerica) - 1):
      if lista_numerica[j] > lista_numerica[j + 1]:
        aux = lista_numerica[j]
        lista_numerica[j] = lista_numerica[j + 1]
        lista_numerica[j + 1] = aux
  return lista_numerica
  



#ORDENAMIENTO POR MEZCLA
def ordenamiento_por_mezcla(lista_numerica):
  if len(lista_numerica) > 1:
    mitad = len(lista_numerica) // 2
    izquierda = lista_numerica[:mitad]
    derecha = lista_numerica[mitad:]
    # print(izquierda, " ** ", derecha , '\n')
    
    #llamada recursiva en cada mitad
    ordenamiento_por_mezcla(izquierda)
    ordenamiento_por_mezcla(derecha)
    
    #iteradores de las sublistas
    i = 0
    j = 0
    # iterador principal
    k = 0
    
    while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
        lista_numerica[k] = izquierda[i]
        i += 1
      else:
        lista_numerica[k] =derecha[j]
        j += 1
      k += 1
    while i < len(izquierda):
      lista_numerica[k] = izquierda[i]
      i += 1
      k += 1
    while j < len(derecha):
      lista_numerica[k] = derecha[j]
      j += 1 
      k += 1 

    return lista_numerica  
    
    



if __name__ == "__main__":
  print(ordenamiento_lineal([55,21,44,89,75,65,2,33,1,0]))
  print(ordenamiento_lineal([1,0]))
  print(ordenamiento_por_mezcla([5,4,8,6]))
  print(ordenamiento_por_mezcla([5,1,0,78,2,98,4,3,1,5]))


