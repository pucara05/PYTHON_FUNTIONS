# si la variable values tiene almacenada una cadena de carateres
#item 1 item 2, item3,item,4item,5 de que manera se puede extraer el
#valor "2" de item 2, como un valor entero.

values=("item 1,item 2,item 3,item 4,item 5,")
dato=int(values.split(",")[1].split(" ")[1])
print(dato)
