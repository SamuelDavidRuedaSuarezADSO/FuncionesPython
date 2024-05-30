# 4. Realiza una función que reciba un número y devuelva una cadena con los nombres de los números
# recibidos, separando cada número con un guion medio. Por ejemplo, si el número recibido es 134,
# la función devolverá la cadena "uno - tres - cuatro".

uno = "uno"
dos = "dos"
tres = "tres"
cuatro = "cuatro"
cinco = "cinco"
seis = "seis"
siete = "siete"
ocho = "ocho"
nueve = "nueve"
cero = "cero"

numT= []

def texto(n):
  for  i in n:
    if i == "1":
      numT.append(uno)
    elif i == "2":
      numT.append(dos)
    elif i == "3":
      numT.append(tres)
    elif i == "4":
      numT.append(cuatro)
    elif i == "5":
      numT.append(cinco)
    elif i == "6":
      numT.append(seis)
    elif i == "7":
      numT.append(siete)
    elif i == "8":
      numT.append(ocho)
    elif i == "9":
      numT.append(nueve)
    elif i == "0":
      numT.append(cero)

num = input("ingresa el numero: ")

texto(num)

res = " - ".join(numT)

print(res)


