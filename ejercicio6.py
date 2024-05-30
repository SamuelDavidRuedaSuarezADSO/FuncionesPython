# 6. Realizar un algoritmo el cual pregunte el nombre de la persona y la edad, tener en cuenta que al
# momento de mostrar la edad en pantalla debe mostrar la fecha de nacimiento de dicha persona.

def edad(n, a):
  actual = 2024
  res = actual-a
  print(f"Hola {n} tu año de nacimineto {res}")

name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))

edad(name, age)