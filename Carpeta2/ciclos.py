#Nombre:Luis-Daniel-Leos-Macias
#Grupo:2-J
#Fecha:11-3-2026
#Metodo que evalua el porcentaje de un alumno
def evaluar_calificacion():
	porcentaje=float(input("ingresa el porcentaje del alumno: "))
	if porcentaje>90:
		print("Grado:A")
	elif porcentaje>80 and porcentaje<=90:
		print("Grado:B")
	elif porcentaje>=60 and porcentaje<=80:
		print("Grado:C")
	else:
		print("Grado:D")
#Metodo que calcula impuestos de una bicicleta
def impuesto_bicicleta():
	precio=float(input("ingrese el precio de la bicicleta: "))
	if precio>100000:
		impuesto=precio*0.15
	elif precio>50000 and precio<=100000:
		impuesto=precio*0.10
	else:
		impuesto=precio*0.05
	print("impuesto a pagar:",impuesto)
#Metodo para verificar si un año es bisiesto
def es_bisiesto():
	año=int(input("ingrese un año: "))
	if(año%4==0 and año%100!=0) or (año%400==0):
		print("El año es bisiesto")
	else:
		print("El año no es bisiesto")
#Metodo que muestra el dia de la semana
def dia_semana():
	num=int(input("Ingrese un numero del 1 al 7: "))
	if num==1:
		print("Domingo")
	elif num==2:
		print("Lunes")
	elif num==3:
		print("Martes")
	elif num==4:
		print("Miercoles")
	elif num==5:
		print("Jueves")
	elif num==6:
		print("Viernes")
	elif num==7:
		print("Sabado")
	else:
		print("Numero invalido")
#Metodo que muestra el mes y sus dias
def mes_dias():
	mes=int(input("Ingrese un numero del 1 al 12: "))
	if mes==1:
		print("Enero tiene 31 dias")
	elif mes==2:
		print("Febrero tiene 28 dias")
	elif mes==3:
		print("Marzo tiene 31 dias")
	elif mes==4:
		print("Abril tiene 30 dias")
	elif mes==5:
		print("Mayo tiene 31 dias")
	elif mes==6:
		print("Junio tiene 30 dias")
	elif mes==7:
		print("Julio tiene 31 dias")
	elif mes==8:
		print("Agosto tiene 31 dias")
	elif mes==9:
		print("Septiembre tiene 30 dias")
	elif mes==10:
		print("Octubre tiene 31 dias")
	elif mes==11:
		print("Noviembre tiene 30 dias")
	elif mes==12:
		print("Diciembre tiene 31 dias")
	else:
		print("Numero invalido")
#Imprimir los primeros 10 numeros naturales
def primeros_naturales():
	for i in range(1,11):
		print(i)
#Imprimir los primeros 10 numeros impares
def primeros_impares():
	contador=1
	num=1
	while contador<=10:
		print(num)
		num+=2
		contador+=1
#Numeros naturales en orden descendente
def naturales_descendentes():
	for i in range(10,0,-1):
		print(i)
#Tabla de multiplicar
def tabla_multiplicar():
	num=int(input("Ingresa un numero: "))
	for i in range(1,11):
		print(num,"x",i,"=",num*i)
#Producto de los digitos de un numero
def producto_digitos():
	num=input("Ingresa un numero: ")
	producto=1
	for digito in num:
		producto*=int(digito)
	print("Producto de los digitos:",producto)
#Menu para probar los metodos
def menu():
	while True:
		print("\nMENU")
		print("1. Evaluar calificacion")
		print("2. Impues bicicleta")
		print("3. Año bisiesto")
		print("4. Dia de la semana")
		print("5. Mes y dias")
		print("6. Primeros 10 naturales")
		print("7. Primeros 10 impares")
		print("8. Naturales descendentes")
		print("9. Tabla de multiplicar")
		print("10. Producto de digitos")
		print("0. Salir")
		opcion=int(input("Seleccione una opcion: "))
		if opcion==1:
		 	evaluar_calificacion()
		elif opcion==2:
			impuesto_bicicleta()
		elif opcion==3:
			es_bisiesto()
		elif opcion==4:
			dia_semana()
		elif opcion==5:
			mes_dias()
		elif opcion==6:
			primeros_naturales()
		elif opcion==7:
			primeros_impares()
		elif opcion==8:
			naturales_descendentes()
		elif opcion==9:
			tabla_multiplicar()
		elif opcion==10:
			producto_digitos()
		elif opcion==0:
				print("Programa terminado")
				break
		else:
			print("Opcion invalida")
menu()
	

	
	
	

	
