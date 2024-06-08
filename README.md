def salon():
    lista = []
    print("Programación de agenda para un salón de fiesta, agregue la fecha o ponga 000 para finalizar")
    fecha = input("Fecha (dd-mm-aaaa): ")    
    while fecha != "000":
        if fecha in [evento[0] for evento in lista]:
            print("Error: La fecha ya está ocupada. Intente con otra fecha.")
        else:
            personas = int(input("Cantidad de personas: "))
            costo = int(input("Agregue el costo del salón: "))
            servicios = input("¿Va a haber costo de servicio? Ponga si o no: ")
            if servicios == "si":
                servicios = int(input("¿Cuánto es el monto del servicio?: "))
            elif servicios == "no":
                servicios = 0
            datos = (fecha, personas, costo, servicios)
            lista.append(datos)
        fecha = input("Agregue la fecha o escriba 000 para finalizar: ")
    return lista

resultado = salon()
print(resultado)
