def datos_santiago():
  print("Me llamo santiago y tengo 21 años")
def datos_raimundo():
  print("Me llamo raimundo y tengo 19 años")
def datos_diego():
  print("me llamo diego y tengo 21 años")
def datos_khristian():
  print("Me llamo khristian y tengo 18 años")
while True:
print("\n--- MENÚ PRINCIPAL ---")
print("1. Función de integrante 1")
print("2. Función de integrante 2")
print("3. Función de integrante 3")
print("0. Salir")
op = input("Seleccione opción: ")
if op == "0":
print("Programa finalizado.")
break
elif op == "1":
  datos_diego() 
elif op == "2": 
  datos_raimundo()
elif op == "3": 
  datos_santiago()
elif op == "4":
  datos_khristian()
else:
print("Opción inválida.")
