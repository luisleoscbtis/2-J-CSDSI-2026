#Luis Daniel Leos Macias 2*J 4/3/26
#zonas horarias
dublin=0
paris=+1
londres=0
tokio=+9
los_angeles=-8
nueva_york=-5
nueva_deli=+5.5
cdmx=-6
hora=float(input("Ingresa el valor de la hora que quieres consultar: "))
print("La hora en las siguientes ciudades seria:")
print("Dublin:",round(hora+dublin, 2))
print("Paris:",round(hora+paris,2))
print("Londres:",round(hora+londres, 2))
print("Tokio:",round(hora+tokio,2))
print("Los Angeles:",round(hora+los_angeles, 2))
print("Nueva York:",round(hora+nueva_york, 2))
print("Nueva Deli:",round(hora+nueva_deli,2))
print("CDMX:",round(hora+cdmx,2))
#conversor de divisas
#china
yuan=0.14
#japon
yen=0.0063
#Estados unidos
dolar=1
#union europea
euro=1.16
#Reino unido
libra=1.33
#pesos
mxn=0.057
pesos=float(input("Ingresa la cantidas de pesos a convertir: "))
print("Los pesos equivalen a:")
print("Dólares:",round(pesos*mxn,2))
print("Euros:",round(pesos*mxn/euro,2))
print("Libras:",round(pesos*mxn/libra,2))
print("Yuan:",round(pesos*mxn/yuan,2))
print("Yen:",round(pesos*mxn/yen,2))