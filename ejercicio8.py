# 8. Realizar un algoritmo el cual sume los ingresos de una empresa mensualmente, teniendo en
# cuenta que se debe saber de qué son las ganancias y se debe pedir al usuario de cuánto dinero
# total se obtuvo de esa ganancia, al final se deberá saber si las ganancias son mayores a las
# ganancias del año pasado, entonces imprimir en pantalla que se obtuvieron más ganancias y hacer
# la respectiva operación para saber de cuanta diferencia fue la ganancia, si las ganancias son
# menores a las ganancias del año pasado imprimir en pantalla el faltante de ganancias para
# completar las ganancias del año pasado. GANANCIAS: Pedir al usuario que ingrese las ganancias
# del año pasado.

def ingresos(ganP):
  ganA = 0
  ganM = []
  for mes in range(1,12):
      ganMes = float(input(f"Ingrese las ganancias del mes {mes}: "))
      ganM.append(ganMes)
      ganA += ganMes
  if ganA > ganP:
      diferencia = ganA - ganP
      print("\nSe obtuvieron más ganancias este año que el año pasado")
      print(f"Diferencia de ganancias respecto al año pasado y este año es de {diferencia}")
  elif ganA < ganP:
      diferencia = ganP - ganA
      print("\nSe obtuvieron menos ganancias este año que el año pasado")
      print(f"Faltante de ganancias para alcanzar las del año pasado: {diferencia}")
  else:
      print("\nLas ganancias de este año son iguales a las del año pasado.")


  print(f"\nGanancias totales del año actual: {ganA}")

ganP = float(input("Ingrese las ganancias del año pasado: "))
ingresos(ganP)