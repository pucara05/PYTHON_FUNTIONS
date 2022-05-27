def calcularCosto(alto,ancho,profundo): 
  volumen=alto*ancho*profundo
  costo=volumen*5
  if alto>30:
     costo=costo+2000
  if costo>10000:
      iva=costo*0.19
      costo=costo+iva
  return costo

def costoTotal(numeroPaquetes,descuento):
    nuevocostoTotal=0
    for i in range(numeroPaquetes):
        alto=float(input())
        ancho=float(input())
        profundo=float(input())
        nuevocostoTotal=nuevocostoTotal+calcularCosto(alto,ancho,profundo)   
    descuento=(descuento*nuevocostoTotal)/100
    nuevocostoTotal=nuevocostoTotal-descuento
    return nuevocostoTotal
