separables  = "La ecuación parece ser de variables separables,\n Ya que el sistema ha determinado que cumple la forma: y' = f(x)g(y)"
bern        = "La ecuación parece ser Bernoulli, Ya que el sistema ha determinado que tiene la forma dy/dx + P(x)y = Q(x)y^n"
bernA       = "La ecuación parece ser Bernoulli con potencia de y a la 1, Ya que el sistema ha determinado que tiene la forma dy/dx + P(x)y = Q(x)y^1"
lDE         = "La ecuación parece ser Linnear Differential Equation \n Ya que el sistema ha determinado que tiene la forma dy/dx + P(x)y = Q(x)" 
errorCode   = "Input Incorrecto. ERROR CODE: 500"
referencias = "El creador del sistemita recomienda usar las siguientes referencias: Calculo de Earl W. Swokowski. Análisis Matemático 1 y 2 de Norman Haaser. Introduction to Ordinary Differential Equations de Shepley L. Ross"

def welcome():
    wilkommen = "Software Creado por Diego Ivan Martinez Acevedo."
    print(wilkommen)
    print("Si no ha leido las instrucciones, por favor leerlas")

def IsLDE():
    print("vamos a tomar mu = e^(integral de P dx)")
    print("ahora vamos a tomar el siguiente formulazo: ")
    print("d/dx [y mu] = mu Q(x)")
    print("Integramos de ambos lados y nos va quedar: ")
    print("[y mu] = integral de mu Q(x) dx")
    print(referencias)

def IsBern():
    print("Primero debemos eliminar la y^n del lado derecho, por lo que multiplicaremos ambos lados por 1/y^n")
    print("Ahora se resuelve como Linnear Differential Equation: ")
    IsLDE()

def IsExact():
    exact = "La ecuación parece ser Exacta" 
    print(exact)
    print("Ya que cumple con la forma: M(x,y) + N(x,y) dy\dx = 0")
    print("Primero verificar que la parcial de M con respecto de y sea igual a la parcial de N con respecto de x")
    print("Para resolver, vamos a integrar M con respecto de x, para obtener f, ahora f nos va quedar un algo + un g(y)")
    print("vamos a derivar f con respecto de y, ahora tendremos un algo + g'(y), podemos comparar esto con N y obtener el valor de g'(y)")
    print("intetgra g'(y) y tendremos g(y) con lo que sustituyendo tendremos la solución")
    print(referencias)

def IsTras():
    tras = "La ecuacion parece ser de Traslacion"
    print (tras)
    print("Primero evaluar que a_1b_2 - b_1a_2 sea distinto de 0, si se cumple puedes continuar")
    print("resolver el siguiente sistema de ecuaciones:")
    print("a_1 h + b_2 k = -c_1")
    print("a_2 h + b_2 k = -c_2")
    print("sustituir los valores obtenidos de k, h en:")
    print("y = v + k ")
    print("x = u + h")
    print("Ahora")
    print("dv/du = a_1 +b_1 z / a_2 + b_2 z")
    print("Donde z = v/u")
    print("resolver por homogenea")
    print(referencias)

def IsSep():
    print("lo más comodo es pasarlo a la forma dy/dx = f(x)g(y)")
    print("de aqui resolver de la siguiente forma:")
    print("dy = f(x)g(y) dx")
    print("1/g(y) dy = f(x) dx")
    print("Realizar las integrales y listo !!")
    print(referencias)

def IsVar():
    var = "La ecuación parece ser de cambio de variables"
    print(var)
    print("Ya que el sistema ha determinado que cumple la forma:")
    print("y' = f(x)+g(x)y")
    print("tomar u = y', por lo tanto u = f(x)+g(x)y")
    print("Resolver para y")
    print("Ahora tomar las derivadas de ambos lados en order de obtener y' ")
    print("ahora sustituimos de regreso con el objetivo de reemplazar y' con u")
    print("Resolver por variables separables, a continuación describo como:")
    IsSep()
    print("No te pierdas en el regreso de variables, recuerda que debe quedar en terminos de x y")
        