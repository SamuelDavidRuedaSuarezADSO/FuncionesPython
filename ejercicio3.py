# 3. Realiza una función recursiva que reciba un número y muestre los números pares entre 1 y el
# número leído.

impares=[]
pares =[]

def recur(n):
  for i in range(1, n):
    if i %2 == 0:
      pares.append(i)
    else:
      impares.append(i)

numero = int(input("Ingresa el numero: "))

recur(numero)

print(f"Los numeros pares son {pares} \n Los numeros impares son {impares}")

