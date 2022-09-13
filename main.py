
#Bienvenido a mi Trivia.
print("Bienvenido a mi trivia sobre computacion.\n")
print("Aqui pondremos a prueba tus conocimientos.\n")
sunombre = input("Ingrese tu nombre: ")
#Pregunta numero uno.
print("\n Hola",sunombre,"responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta: \n")
print("1. Entre los primeros habitantes del Peru tenemos a los pescadores de ... en la region de la Libertad.")
print("\na) Lauricocha")
print("b) Guitarrero")
print("c) Nanchoc")
print("d) Paijan")
#Validamos los datos.
respuesta1 = input("\nTu respuesta es: ")
while respuesta1 not in ("a", "b", "c", "d"):
  respuesta1 = input("Debes responder a, b, c o d (En minusculas). Ingresa nuevamente tu respuesta: ")
  
if respuesta1=="d":
  print("\nBuen trabajo",sunombre,"sigamos :)")
else:
  print("\nRespuesta incorrecta",sunombre,":(")
#Pregunta numero dos.
print("\n2. El primer emperador del Tahuantinsuyo fue: ")
print("\na) Manco Capac")
print("b) Huiracocha")
print("c) Pachacutec")
print("d) Huayna Capac")
#Validamos los datos.
respuesta2 = input("\nTu respuesta es: ")
while respuesta2 not in ("a", "b", "c", "d"):
  respuesta2 = input("Debes responder a, b, c o d (En minusculas). Ingresa nuevamente tu respuesta: ")
  
if respuesta2=="c":
  print("\nBuen trabajo",sunombre,"sigamos :)")
else:
  print("\nRespuesta incorrecta",sunombre,":(")
#Pregunta numero tres.
print("\n3. Cual de las siguientes cuidades peruanas se ubica a mayor altitud sobre el nivel del mar: ")
print("\na) La Oroya")
print("b) Cusco")
print("c) Cajamarca")
print("d) Puerto Maldonado")
#Validamos los datos.
respuesta3 = input("\nTu respuesta es: ")
while respuesta3 not in ("a", "b", "c", "d"):
  respuesta3 = input("Debes responder a, b, c o d (En minusculas). Ingresa nuevamente tu respuesta: ")
  
if respuesta3=="a":
  print("\nBuen trabajo",sunombre,"sigamos :)")
else:
  print("\nRespuesta incorrecta",sunombre,":(")
#Pregunta numero cuatro.
print("\n4. El Peru tuvo mas conflictos armados con: ")
print("\na) Colombia")
print("b) Ecuador")
print("c) Brasil")
print("d) Chile")
#Validamos los datos.
respuesta4 = input("\nTu respuesta es: ")
while respuesta4 not in ("a", "b", "c", "d"):
  respuesta4 = input("Debes responder a, b, c o d (En minusculas). Ingresa nuevamente tu respuesta: ")
  
if respuesta4=="b":
  print("\nBuen trabajo",sunombre,":)")
else:
  print("\nRespuesta incorrecta",sunombre,":(")
    
print ("\nAcabo todo verdaderamente eres un mostro en cultura general.")
print ("\nThank you! :)")
print ("\nGob job! :)")