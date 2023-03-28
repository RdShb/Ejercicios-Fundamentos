# Ejercicio 1

### Calcular la letra del DNI Español

**Entrada** -> DNI = numero a ingresar de 8 digitos
**Proceso** -> 
Pedir al usuario el número de DNI (sin la letra).
Calcular el resto de la división del número de DNI entre 23.
Asociar cada posible resto con una letra según la tabla de correspondencia:

- Resto 0: T
- Resto 1: R
- Resto 2: W
- Resto 3: A
- Resto 4: G
- Resto 5: M
- Resto 6: Y
- Resto 7: F
- Resto 8: P
- Resto 9: D
- Resto 10: X
- Resto 11: B
- Resto 12: N
- Resto 13: J
- Resto 14: Z
- Resto 15: S
- Resto 16: Q
- Resto 17: V
- Resto 18: H
- Resto 19: L
- Resto 20: C
- Resto 21: K
- Resto 22: E
**Salida** -> Mostrar al usuario la letra correspondiente al resto 

# Ejercicio 2

### Calcular el salario de un empleado

**Entrada** ->  Horas = horas trabajadas por mes
            salario = sueldo por hora
**Proceso** ->
    Pedir al usuario que introduzca el número de horas trabajadas en el mes.
    Pedir al usuario que introduzca el salario por hora del empleado.
    Calcular el salario bruto multiplicando el número de horas trabajadas por el salario por hora.
    Calcular la cantidad de impuestos a pagar sobre el salario bruto.
**Salida** -> Mostrar el sueldo total multiplicando horas * sueldo/horas y restando los impuestos

# Ejercicio 3

### Determinar la ruta para llegar a una ciudad por avión.

**Entrada** ->  Ciudad_destino
            Ciudad_origen
**Proceso** -> 
    Pedir al usuario que introduzca la ciudad de origen y la ciudad de destino.
    Buscar en una base de datos de aeropuertos las rutas posibles para llegar de la ciudad de origen a la ciudad de destino.
    Seleccionar la ruta mas rapida disponible
    Si no hay ninguna disponible directa, buscar la mas rapida con conexiones
**Salida** -> indica la mejor ruta

# Ejercicio 4

### Calcula el área y perímetro de un círculo dado su radio.

**Entrada** -> Radio
**Proceso** -> Dado el Radio de un circulo, lo multiplico por 2π para calcular el perimetro, para calcular el area lo elevo al cuadrado y lo multiplico por π

```
  	perimetro = 2 * pi * Radio
    area = pi * radio ** 2
```

 

**Salida** -> mostrar perimetro y area

# Ejercicio 5

### Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor.

**Entrada** -> numeros = lista de numeros
**Proceso** ->  Creo la variable *menor* y *mayor*.

Itero por la lista de numeros, en caso de que el numero por el que se este iterando sea mayor a *mayor* o menor a *menor*, lo copio dentro de esa variable

```
 declaro mayor y menor 
 for i in numeros:
    si valor(i) < menor
        menor = valor(i)
    si valor(i) > mayor
        mayor = valor(i) 
```

**Salida** -> 
    mayor = numero mayor
    menor = numero menor

# Ejercicio 6

### Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor.

**Entrada** -> celsius = input(celsius)
**Proceso** -> Dado un valor Celsius de temperatura, lo multiplico por 1.8 y le agrego 32 para conseguir su equivalente en Farenheit
  `   Farenheit = celsius*1.8 + 32` 
**Salida** -> printear(Farenheit)

# Ejercicio 7

### Dado un número entero, crea un algoritmo que determine si es par o impar

**Entrada** -> numero = numero ingresado
            Par
**Proceso** -> Divido el numero por 2, en caso de que el resto sea 0 el numero es par, caso contrario es impar

```
 resto = numero%2
    si resto == 1
        Par = 0
    sino 
        par = 1
```

**Salida** -> Par == 1 -> Printear par
                    sino printear impar

# Ejercicio 8

### Crea un algoritmo que determine si un año es bisiesto o no.

**Entrada** -> año = año ingresado
**Proceso** -> Si el año ingresado es divisible por 400 es biciesto. Si no es divisible por 400 y por 100 pero si lo es por 4, es biciesto. En todos los otros casos no lo es.

```
 si año%400 == 0
       	Biciesto = 1
   elseif año%4 == 0 y año%100 != 0
   		biciesto = 1
   else 
        biciesto = 0 
```

**Salida** -> Printear es biciesto si biciesto == 1 sino no es biciesto

# Ejercicio 9

### Crea un algoritmo que determine si una cadena de texto es un palíndromo o no.

**Entrada** --> palabra = ingresar texto
**Proceso** -> Utilizo una lista auxiliar donde escribire cada letra de la palabra original pero en orden contrario, empezando por la ultima y terminando en la primera.

Luego comparo cada letra en ambas listas y en caso de que todas las letras sean iguales la palabra es un palindromo.

```
   for i in palabra
                arbalap[i] = palabra[len(palabra) -i]
            for i in arbalap
                if palabra[i] =! arbalap[i]
                    return 0
            return 1
```


**Salida** -> si return 1 -> palindromo, sino no es

# Ejercicio 10

### Dada una lista de nombres, crea un algoritmo que ordene la lista alfabéticamente.

***Entrada*** -> lista[1,2,3,4] donde cada numero es un nombre 
**Proceso** -> Primero leo la primer letra de cada nombre y calculo el valor ASCII de ella, luego ordeno las palabras segun el valor de su primer letra.

En caso de que haya 2 letras con el mismo valor repito el procedimiento con la siguiente letra

```
  lista_ordenada[]
            for i in lista
                leer la primer letra
            si las letras son distintas, escribir en lista_ordenada[] el nombre con la menor letra
            sino leer la segund y loopear
```


**Salida** -> print lista ordenada

# Ejercicio 11

### Crea un algoritmo que calcule el factorial de un número entero.

**Entrada** -> numero = numero ingresado
            Factorial = 1
**Proceso** -> Dado el numero ingresado, se multiplica el numero una vez por cada valor menor a ese numero.

```
while(numero > 1): 
	factorial = factorial*numero
	numero -= 1
```

**Salida** -> imprimir factorial

# Ejercicio 12

### Dado un número entero, crea un algoritmo que determine si es primo o no.

**Entrada** -> numero = numero ingresado
**Proceso** ->  Solo pueden ser primos los numeros mayores o iguales a 2 por lo que descarto los menores a el, luego declaro el 2 como primo.

Por ultimo calculo el resto de dividir ese numero por todos los valores menores a el, en caso de que el resto sea 0 ese numero no es primo ya que es divisible por un numero distinto a el mismo.

```
si numero <=1
	no es primo
si numero == 2
	es primo
else 
	for i in numero
		si numero%i == 0
			no es primo
		sino 
			es primo
```


**Salida** -> dice si es primo o no

# Ejercicio 13

### Crea un algoritmo que calcule el área y volumen de un cubo dado su lado.

**Entrada** -> lado = lado del cubo
**Proceso** -> Una vez dado el lado del cubo se lo potencia al cuadrado y multiplica por 6 para calcular el area y luego el lado se lo potencia al cubo para calcular el volumen

```
area = 6 * lado^2
volumen = lado ^ 3
```


**Salida** -> el area es *area* y el volumen del cubo es *volumen*

# Ejercicio 14

### Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista

**Entrada** -> lista[] = lista de numeros
            total_par = total de numeros par (int)
**Proceso** -> Pido una lista de numeros al usuario.

Divido cada valor de la lista y, en caso de que el resto de ese valor sea 0, sumo ese numero al total_par.

```
    for i in lista[]
        if valor(i)%2 == 0
            total_par = total_par + valor(i)
            i = i+1
        else
            i = i+1
```


**Salida** -> imprimir total_par

# Ejercicio 15

### Crea un algoritmo que determine si un número es positivo, negativo o cero.

**Entrada** -> numero = numero ingresado
           tipo = tipo de numero (string)
**Proceso** -> Leo el numero ingresado e imprimo al usuario si el numero es mayor, igual o menor a cero

```
     if numero < 0 
        tipo = "negativo"
    elif numero > 0
        tipo = "positivo"
    else 
        tipo = "0"
```


**Salida**-> imprimir tipo

# Ejercicio 16

### Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista

**Entrada** -> lista[] = lista de numeros
            total = 0
**Proceso** -> Sumo la totalidad de los numeros en la lista y luego los divido por la cantidad de numeros en ella

```
    for i in lista
        total = total + i
    media = total/len(lista[])
```


**Salida** -> imprimir lista

# Ejercicio 17

##### Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.

**Entrada** ->  rng = numero al azar entre 1 y 100
            numero = numero usuario
**Proceso** -> Genero un numero al azar **rng**  y pido al usuario un numero.

Lo leo y le comunico al usuario si el numero es mayor, menor o igual al **rng**, en caso de no ser igual vuelvo a pedir otro numero hasta que sean iguales

```
leer numero
   while numero != rng
            si numero > rng
                "el numero es menor, prueba otra vez"
                pedir nuevo numero
            else 
                "el numero es mayor, prueba otra vez"
                pedir nuevo numero
    "Felicidades, el numero es rng"
```

**Salida** -> Felicidades, el numero es *rng*

# Ejercicio 18

### Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto.

**Entrada** ->  palabra1 = palabra original
            palabra2 = palabra a determinar 

si es un anagrama de palabra1
**Proceso** -> Primero creo una lista auxiliar para cada palabra y escribo en ellas las letras de cada palabra pero ordenadas alfabeticamente en lugar de en su orden original.

En caso de que las palabras sean anagramas de la otra, las letras utilizadas seran iguales en ambos casos.

Si ambas listas auxiliares son iguales, las palanras son anagramas

```
letras1[] = escribir cada letra de palabra1 en una lista y ordenarlas alfabeticamente
    letras2[] = escribir cada letra de palabra2 en una lista y ordenarlas alfabeticamente
    anagrama -> si letras1 == letras 2
            anagrama = 1
        sino
            anagrama = 0
```

**Salida** -> si anagrama == 1-> las palabras son anagramas, sino no lo son

# Ejercicio 19

### Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista.

**Entrada** -> numeros[] = cadena de numeros
**Proceso** -> Luego de pedir una cadena de numeros, creo una cadena auxiliar numeros2.

Por cada numero de la cadena original veo los valores de la segunda cadena y, en caso de no estar en ella, lo escribo en numeros2, luego paso al siguiente numero.

Una vez se termine de iterar la lista original imprimo la lista numeros2

```
numeros2[] = for i in numeros 
	si valor(i) no esta en numeros2[]
		escribirlo
		i = i+1
	sino
		i = i+1
```

**Salida** -> imprime en pantalla *numeros2[]

# Ejercicio 20 

### Crea un algoritmo que determine si un número es capicúa o no.

**Entrada** ->  numero = numero a ingresar
            numero_inverso[] = lista
**Proceso** -> Primero escribo cada digito del numero original en una lista en orden.

​					Luego creo una nueva lista numero_inverso donde escribo cada digito en orden contrario, iniciando por el ultimo hasta llegar al primero

Al finalizar comparo ambas listas y si son iguales el numero es capicúa

**Algoritmo** ->

```
 nuevo_numero[] = escribir cada digito del numero en un valor de la lista
    for i in nuevo_numero[]
        numero_inverso[i] = nuevo_numero[len(nuevo_numero) - i]
    si numero inverso[] es igual a nuevo_numero[], el numero es capicua 
```

**Salida** -> indica si el numero es capicua   