def Datos():
	print("bienvenido a la veterinaria, porfavor ingrese los datos solicitados o ingrese 000 para terminar")
	completos=[]
	incompletos=[] 
	nombre=input("ingrese su nombre: ")
	while nombre!="000":
		apellido=input("ingrese su apellido: ")
		dni=input("ingrese su DNI: ")
		dueño=input("¿es el dueño del animal? (Si o No): ")
		nom_ani=input("ingrese el nombre de la mascota: ")
		edad=input("ingrese la edad de la mascota: ")
		print("Porfavor siga ingresando los datos solicitados o ingrese 000 para terminar")
		nombre=input("ingrese su nombre: ")
		if (nombre==""or apellido==""or dni==""or dueño== "" or nom_ani=="" or edad== ""):
			Dat_inc=nombre,apellido,dni,dueño,nom_ani,edad
			incompletos.append(Dat_inc)
		else:
			Dat_com=nombre,apellido,dni,dueño,nom_ani,edad
			completos.append(Dat_com)
	return completos,incompletos
Dat=Datos()
print(Dat[0])
print("-----------------------")
print(Dat[1])
