#nombre:Luis Daniel Leos Macias
#Grupo:2-J
#Fecha:12-3-2026
#Encontrar que elementos de una lista suman cero
#Escribe una clase de python que encuentre 3 elementos que sumen cero
#Los elementos se encuentran en una lista y son numeros enteros+-
#Codigo
class SumaCero:
	def encontrar(self,lista):
		for a in lista:
			for b in lista:
				for c in lista:
					if a+b+c==0:
						print(a,b,c)
numeros=[-1,0,1,2,-1,-4]
obj=SumaCero()
obj.encontrar(numeros)
