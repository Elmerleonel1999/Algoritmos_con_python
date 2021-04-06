def nTablaMultiplicar(nT):
  for i in range(13):
    print(f" {nT} * {i} = ", nT * i)
  print('\n')

def nTablaMultiplicarRango(nT, rango):
  for i in range(rango + 1):
    print(f" {nT} * {i} = " , nT * i)
  print('\n')

def nTablasMultiplicar(nT_I, nT_F):
  for i in range(nT_I, nT_F + 1):
    for j in range(13):
      print(f" {i} * {j} = ", i * j)
    print('\n')

if __name__ == "__main__":
  
  nTablaMultiplicar(5)
  nTablasMultiplicar(2,3)
  nTablaMultiplicarRango(4,20)