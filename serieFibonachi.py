#Fibonachi: 0 + 1 = 1,
          # 1 + 1 = 2,
          # 1  + 2 = 3,
          # 2 + 3 = 5 ,
          # 3 + 5 = 8
# ---- > se le da un rango de ciclos al algoritmo y este sumara el numero anterior con el actual.

def Fibonachi(n):
  rs = []
  x = 0
  y = 1
  z = 1
  for i in range(n + 1):
    z = x + y
    rs.append(z)
    print(x, "  ", y , "  ", rs)
    x = y
    y = z
  

if __name__ == "__main__":
  
  Fibonachi(15)