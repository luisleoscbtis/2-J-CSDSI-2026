#Nombre: Luis Daniel Leos Macias
#Grupo: 2ºJ
#Fecha: 21/2/26
#Programa: Generador de CURP y RFC
#Numero de practica: 2

a=input("Escribe tu nombre completo: ").upper()
b=input("Bien!, ahora escribe tu fecha de nacimiento (solo 6 digitos A/M/D): ")
c=input("Ahora ¿cual es tu genero? (H/M): ").upper()
d=input("ingresa el Estado en el que naciste (solo 2 letras): ").upper()
partes=a.split()
nombres_comunes=["JOSE","MARIA","MA","MA.","J","J.","JOSE.","LUIS"]
if partes[0] in nombres_comunes and len(partes)>3:
		nombre=partes[1]
else:
		nombre=partes[0]
ap_paterno=partes[-2]
ap_materno=partes[-1]
vocal="X"
for letra in ap_paterno[1:]:
	if letra in "AEIOU":
		vocal=letra
		break
con1="X"
for letra in ap_paterno[1:]:
	if letra not in "AEIOU":
		con1=letra
		break
con2="X"
for letra in ap_materno[1:]:
	if letra not in "AEIOU":
		con2=letra
		break
con3="X"
for letra in nombre[1:]:
	if letra not in "AEIOU":
		con3=letra
		break
curp=(ap_paterno[0]+vocal+ap_materno[0]+nombre[0]+b+c+d+con1+con2+con3+"00")
curp=curp.upper()
print("Tu CURP es:",curp)
rfc=(ap_paterno[0]+vocal+ap_materno[0]+nombre[0]+b+"XXX")
print("Tu RFC es:",rfc)








