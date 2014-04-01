def sumar(x,y):
	res = x + y
	return res

def restar(x,y):
	res = x - y
	return res

def multiplicar(x,y):
	res = x * y
	return res

def dividir(x,y):
	res = x / y
	return res

print """Eligi la clase de operacion a realizar:\n
 1-Sumar\n 2-Restar\n 3-Multiplicar\n 4-Dividir\n"""

opcion = int(input("Diganos su opcion:"))

num1 = int(input("Digite el primer numero:"))
num2 = int(input("Digite el segundo numero:"))

if opcion == 1:
	respuesta = sumar(num1,num2)
elif opcion == 2:
	respuesta = restar(num1,num2)
elif opcion == 3:
	respuesta = multiplicar(num1,num2)
else:
	respuesta = dividir(num1,num2)

print "El resulado es %d" % (respuesta)