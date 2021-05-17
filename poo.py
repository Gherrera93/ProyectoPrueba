class Persona :
	def __hablar__ (self,mensaje):
	   print (mensaje)
	def __sumar__ (self,valores):
	   print (valores)

class Administrador (Persona):
	def __gestionar__ (self,mensaje):
	   print (mensaje)

Lucia = Administrador()
Lucia.__gestionar__("Soy administrador")
Lucia.__hablar__("Hola soy Lucia")
Juan = Persona()
Juan.__hablar__("Hola")

Gema = Persona()
Gema.__sumar__("Ingrese valores para la operacion")
