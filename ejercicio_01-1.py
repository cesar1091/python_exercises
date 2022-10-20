def desencriptando_mensajes(horas, mensaje_desencriptado):

  message = mensaje_desencriptado.lower()
  message_final = ""
  horas = -1*horas
  for i in message:
    if (ord(i)>=97) & (ord(i)<=122):
      c = x + (horas)%(122-97+1)
      c = 97 + (c-97)%(122-97+1)
    else:
      desencriptar = {ord('$'):ord('.'),
                      ord('&'):ord(','),
                      ord(','):ord('&'),
                      ord('/'):ord(' '),
                      ord(' '):ord('/')}
      c = desencriptar.get(ord(i),ord(i))
    message_final.join(chr(c))
  return message_final




a=int(input("horas:"))
b=str(input("mensaje_encriptado:"))

desencriptando_mensajes(a, b)

  
  #def rotar(x,horas):
  #  horas=-1*horas
  #  if (x>=97) & (x<=122):
  #    c=x+(horas)%(122-97+1)
  #    c=97+(c-97)%(122-97+1)
  #  else:
      #d={ord('$'):ord('.'),ord('.'):ord('$'),ord('&'):ord(','),ord(','):ord('&'),ord('/'):ord(' '),ord(' '):ord('/')}
  #    desencriptar={ord('$'):ord('.'),ord('&'):ord(','),ord('/'):ord(' ')}
  #    c=desencriptar.get(x,x)      
  #  return chr(c)

  #def encriptar(horas,mensaje_desencriptado):
  #  return ''.join([rotar(ord(i),horas) for i in list(mensaje_desencriptado.lower())])
  
  #a=int(input("horas:"))
  #b=str(input("mensaje_encriptado:"))
  







  return encriptar(a, b)
