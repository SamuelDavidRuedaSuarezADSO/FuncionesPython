# 2. Realiza una función que reciba una palabra y devuelva un diccionario donde las claves sean las
# diferentes letras que se encuentran en la palabra y los valores sean el número de veces que se
# repite cada letra en la palabra.+


def observar(p):
  a = "a"
  e = "e"
  o = "o"
  sumaA = 0
  sumaE = 0
  sumaO = 0
  for i in p:
    if i == a:
      sumaA += 1
    elif i == e:
      sumaE += 1
    elif i == o:
      sumaO += 1
  total ={
    a: sumaA,
    e: sumaE,
    o: sumaO
  }
  return total

palabra = "aerodinamico"

print(observar(palabra))

