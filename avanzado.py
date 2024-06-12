def datos():
	print("bienvenido a la veterinaria, ¿desea crear una lista de datos? Si para comenzar y No para finalizar")
	lista=[]
	inicio=input("ingrese si o no: ").upper()
	while inicio!="NO":
		nombre=input("ingrese su nombre: ")
		apellido=input("ingrese su apellido: ")
		dni=input("ingrese su DNI: ")
		dueño=input("¿es el dueño del animal? (Si o No): ")
		nom_ani=input("ingrese el nombre de la mascota: ")
		edad=input("ingrese la edad de la mascota: ")
		vacunas=input("¿cuantas vacunas tiene?: ")
		inicio=input("¿desea crear otra lista de datos? Si para continuar y No para finalizar: ").upper()
		datos= nombre,apellido,dni,dueño,nom_ani,edad,vacunas
		lista.append(datos)
	return lista 

def separar_datos(lista):
	completos=[]
	incompletos=[]
	for elemento in lista:
		if (elemento[0]==""or elemento[1]==""or elemento[2]==""or elemento[3]== "" or elemento[4]=="" or elemento[5]== ""or elemento[6]== ""):
			incompletos.append(elemento)
		else:
			completos.append(elemento)
	return [completos,incompletos]
dat=datos()
listas= separar_datos(dat)
print("--------------------------")
print("completos ",listas[0])
print("--------------------------")
print("incompletos ",listas[1])
print("--------------------------")

def edad_acendente(lista):
	print("lista acendente de edad de los animales")
	lista.sort(key=lambda lista: lista[5])
	print("________________________________________")
	print(" Nombre del dueño: ",lista[0]," Dni: ",lista[2]," nombre del animal: ",lista[4]," edad: ",lista[5])
	print("________________________________________")
	return lista
edad=edad_acendente(dat)
