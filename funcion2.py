# funciones prederteminadas
#input
#print
##funcion max() => determinael maximo valor de un grupo o lista de elementos
numero=max(2,3,8,4,9,5,7,6,12,9,21,1,11)
print("el maximo valor es: ", numero)
#lista1=max([1,50,42,38,2,7,73,45,51,53])
#print("el maximo numero de la lista es: ", lista1)
lista1=[1,50,42,38,2,7,73,45,51,53]
print("el maximo numero de la lista es: ",max(lista1))

lista2=["a","x","z","q","t","v","ñ"]
print("el maximo valor de la lista es: ", max(lista2))

lista3=[1,2,3,"a","b","c"]
#print("el maximo valor de la lista es: ", max(lista3)) da error ya que max no funciona por que no puede establecer numeros y letras al mismo tiempo

print("---------------------------------")

#funcion min() --> determina el minimo valor de un grupo o lista de elementos
print("el minimo numero de la lista1 es: ", min(lista1))
print("el minimo valor de la lista 2 es: ",min(lista2))
print("------------------------")

#funcion divmod() --> devuelve el cociente y el residuo al dividir el numero a por el numero b

print(divmod(12,3))
# funcion len() --> devuelve la longitud de un objeto
print("----------------")
lista4=[5,2,7,9,8,71,82,9,10,54]
print(len(lista4))
print("-------------")
uis="universida industrial de santander "
print(len(uis))
print("-------------")
nombre="daniel antonio cardenas villamizar"
#print(len(nombre))
print("------------------")
#funcion ord() --> convierte la cadena que representa un caracter en un entero
print(ord("a"))
print(ord("m"))
print("--------------------")
# upper() --> convierte a mayuscula el contenido de la variable
#print(nombre.upper())
print("-------------")
print(nombre.lower())
print("---------------------------")
a="carlos"
print(a.capitalize())





