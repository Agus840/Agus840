#ESTAS SON LAS FUNCIONES 
"""ESTA FUNCION SIRVE PARA CARGAR LOS DATOS"""
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
		edad=int(input("ingrese la edad de la mascota: "))
		vacunas=int(input("¿cuantas vacunas tiene?: "))
		inicio=input("¿desea crear otra lista de datos? Si para continuar y No para finalizar: ").upper()
		datos= nombre,apellido,dni,dueño,nom_ani,edad,vacunas
		lista.append(datos)
	return lista


"""ESTA FUNCION SIRVE PARA SEPARAR LOS DATOS COMPLETOS Y INCOMPLETOS"""

def separar_datos(lista):
	completos=[]
	incompletos=[]
	for elemento in lista:
		if (elemento[0]==""or elemento[1]==""or elemento[2]==""or elemento[3]== "" or elemento[4]=="" or elemento[5]== ""or elemento[6]== ""):#SI ALGUNO ESTA VACIO O, EL OTRO O, EL OTRO ENTRA EN "INCOMPLETOS" SINO ENTRA EN "COMPLETOS"
			incompletos.append(elemento)
		else:
			completos.append(elemento)
	return [completos,incompletos]
	
	
"""ESTA FUNCION SIRVE PARA DAR LA EDAD DE LOS ANIMALES DE MAYOR A MENOR"""

def edad_acendente(lista):
  return lista.sort(reverse=True,key=lambda lista: lista[5])
 
 

def vacuna(lista):
	return lista.sort(reverse=True,key=lambda lista: lista[6])
  
def listar_opciones():
	print("")
	print("*----- MENU -----*") 
	print("") 
	print("0) SALIR") 
	print("1) CARGAR DATOS") 
	print("2) SEPARAR DATOS COMPLETOS DE INCOMPLETOS") 
	print("3) EDAD DE MAYOR A MENOR DE LOS ANIMALES") 
	print("4) CANTIDAD DE VACUNAS DE MAYOR A MENOR DE LOS ANIMALES") 
	print("")
	print("*---------------*") 
	print("")



def menu():
	listar_opciones()
	opcion=int(input("ingrese una opcion: "))
	while opcion!= 0:
		if opcion == 1:
			lista=datos()
		elif opcion== 2:
			lista_separar=separar_datos(lista)
			print("completos: ",lista_separar[0])
			print("incompletos: ", lista_separar[1])
		elif opcion == 3:
			edad_acendente(lista)
			print(lista)
		elif opcion == 4:
			vacuna(lista)
			print("lista ordenada por vacunas",lista)
		listar_opciones()	
		opcion=int(input("ingrese una opcion: "))
		
		

  
  
#ESTE ES EL PROGRAMA PRINCIPAL 
lista=[]
menu()

