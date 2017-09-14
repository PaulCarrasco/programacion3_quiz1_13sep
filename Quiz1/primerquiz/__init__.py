i = 0
while i < 3:
  nombre =input("Introduce Palabra secreta ")
  if nombre == "gato":
      print(nombre," Es Palabra correcta!!")
      break
  else:
      print (nombre," Palabra es Incorrecta")


  i += 1

if i == 3:
  print("Has sobrepasado el numero de intentos")
