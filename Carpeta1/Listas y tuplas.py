#Luis Daniel Leos Macias 2*J 4/3/26
#crear una tupla con 3 elementos: 10 "Hola" y 3.14
tupla=(10,"Hola",3.14)
print(tupla)
#La tupla (1,2,3,4,5) accede y escribe el tercer elemento
tupla=(1,2,3,4,5)
print(tupla[2])
#concatena las tuplas y almacena el resultado en una tupla nueva
tupla1=(1,2,3)
tupla2=(4,5)
tupla_final=tupla1+tupla2
print(tupla_final)
#Desempaqueta la tupla en tres variables y escribe sus valores
tupla=('a','b','c')
var1,var2,var3=tupla
print(var1,var2,var3)
#verifica si el elemento 7 existe en la tupla (1,3,5,7,9)
tupla=(1,3,5,7,9)
existe=7 in tupla
print(existe)
#crea una tupla (0,1,2,3,4,5) y escribe los elementos del indice 2 a 4 con slice
tupla=(0,1,2,3,4,5)
resultado=tupla[2:5]
print(resultado)
#Encuentra la longitud de una tupla (10,20,30,40,50)
tupla=(10,20,30,40,50)
length=len(tupla)
print(length)
#crea una tupla y repitela 3 veces
tupla=(1,2,3)
resultado=tupla*3
print(resultado)
#convierte la lista [1,2,3] a tupla
lista=[1,2,3]
tupla=tuple(lista)
print(tupla)
#Encuentra loa valores minimo y maximo de la tupla (5,12,3,8,15)
tupla=(5,12,3,8,15)
valor_minimo=min(tupla)
valor_maximo=max(tupla)
print("Minimo:",valor_minimo,"Maximo:",valor_maximo)






