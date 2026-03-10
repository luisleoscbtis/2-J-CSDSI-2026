#Nombre: Luis Daniel Leos Macias
#Grupo: 2ºJ
#Fecha: 22/2/26
#Nombre de la practica: Visa y Pasaporte
#Numero de practica: 3
print("Hola a que lugar quisiera ir?")
print("Las opciones son: Estados unidos, Europa, Japon, Peru, Medio oriente")
lugar=input("Ingresa el lugar que has seleccionado: ")
vigencia=int(input("Que fecha de validez tiene tu pasaporte(1,2,5 o 10 años): "))
edad=int(input("Ok, ahora ingresa tu edad: "))
#Costo del pasaporte
if vigencia==1:
	costo_pasaporte=815
elif vigencia==2:
	costo_pasaporte=1585
elif vigencia==5:
	costo_pasaporte=2155
elif vigencia==10:
	costo_pasaporte=3780
else:
	costo_pasaporte=0
#Visa
if lugar=="Estados Unidos":
	visa=3200
elif lugar=="Europa":
	visa=1800
elif lugar=="Japon":
	visa=0
elif lugar=="peru":
	visa=0
elif lugar=="Medio Oriente":
	visa=2500
else:
	visa=0
total=costo_pasaporte+visa
print("Calculando los costos..$$")
print("Lugar de destino:",lugar)
print("Costo del pasaporte: $",costo_pasaporte)
print("Costo de la visa: $",visa)
print("El total a pagar es: $",total)




