## Para de variables separables o cambio de variable, usar la siguiente sintaxis: y' = ECUACIÓNFELIZ
## Para Beronulli, Linnear Differential Equation, Exact y Traslación se puede usar las siguientes sintaxis:
- ALGO = y' F(x)y
- y' + F(x)y = Q(x)
- y' + F(x)y = Q(x)y^n
## Para Exactas usar el siguiente formato 0 = M(x,y) + N(x,y)
## Solo usar x & y como variables

- ** Ecuaciones usadas para probar:
- 0 = 2xe^y + e^x + (x^2+1)e^y y' : Es Exacta
- 12x^12 = y' + 8x^3y : Es Linnear Dif. Eq
- y' + 3y = 2xe^-3x : Es Linnear Dif. Eq
- y' = x + y : es de cambio de varibles
- y' xy = -xy^2 : Es Bernoulli

## ¿Cómo correr el programa ?
El programa está construido en modulos, el archivo app.py es el que se debe ejecutar, este "reune" los demás modulos y los ejecuta en el orden correcto, por esto, TODOS LOS ARCHIVOS deben estar en la misma carpeta, de lo contrario te lanzará una alerta indicando que no se encuentra algún modulo

