def Menu ():

	print ("*****************************************")
	print ("*             BIENVENIDOS               *")
	print ("*            MENU PRINCIPAL             *")
	print ("*                                       *")
	print ("*  1. SUMA                              *")
	print ("*  2. RESTA                             *")
	print ("*  3. MULTIPLICACION		        *")
	print ("*  4. DIVISION			        *")
	print ("* 				        *")
	print ("*  ELIJA UNA OPCION:                    *")
	print ("*				        *")
	print ("*****************************************")
	
	opcion= input('SU OPCION ES:')
	return opcion

def suma (num1, num2):
	return num1 + num2
def resta (num1, num2):
	resultado= num1 - num2
	return resultado
def multiplicacion (num1, num2):
	resultado= num1 * num2
	return resultado
def division (num1, num2):
	if num2==0:
	  print ('ERROR NO SE PUEDE REALIZAR LA OPREACION')
	else:
		resultado= num1 / num2
		return resultado
 
op=Menu()
print ("Ingrese primer numero:")
v1=int(input())
print ("Ingrese segundo numero")
v2= int(input ())

if op=='1':
   r=suma(v1,v2)
   print ('el resultado es: ',r)
elif op=='2':
     r= resta(v1,v2)
     print (r)
elif op=='3':
     r=multiplicacion(v1,v2)
     print (r)
elif op=='4':
     r=division(v1,v2)
     print (r)



