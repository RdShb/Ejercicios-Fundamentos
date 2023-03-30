Proceso:

**Paso 1**: Definir el problema

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Paso 3**: Escribir el pseudocódigo.

# Ejercicio 1

### Calcular la letra del DNI Español

**Paso 1**: Definir el problema:

**¿Cómo se calcula la letra del DNI?**

El número del DNI **debe tener 8 dígitos**. Para calcular la letra del Documento Nacional de Identidad (DNI) español, se utiliza un algoritmo que se basa en el número de identificación. El procedimiento es el siguiente:

1. Dividir el número de identificación entre 23.
2. Tomar el resto de la división anterior.
3. Consultar una tabla que asocia cada resto con una letra. La tabla es la siguiente

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> DNI = numero a ingresar de 8 digitos
**Proceso** -> 
Pedir al usuario el número de DNI (sin la letra).
Calcular el resto de la división del número de DNI entre 23.
Asociar cada posible resto con una letra según la tabla de correspondencia

**Salida** -> Mostrar al usuario la letra correspondiente al resto 

**Paso 3**: Escribir el pseudocódigo.

| Resto | Letra |
| --- | --- |
| 0 | T |
| 1 | R |
| 2 | W |
| 3 | A |
| 4 | G |
| 5 | M |
| 6 | Y |
| 7 | F |
| 8 | P |
| 9 | D |
| 10 | X |
| 11 | B |
| 12 | N |
| 13 | J |
| 14 | Z |
| 15 | S |
| 16 | Q |
| 17 | V |
| 18 | H |
| 19 | L |
| 20 | C |
| 21 | K |
| 22 | E |

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

**Paso 1**: Definir el problema

Para resolver el problema de calcular el área y perímetro de un círculo dado su radio, se pueden utilizar las siguientes fórmulas matemáticas:

- El perímetro o circunferencia del círculo se calcula como: P = 2 * pi * r, donde "pi" es una constante que representa la relación entre la circunferencia y el diámetro de cualquier círculo (aproximadamente igual a 3.14159), y "r" es el radio del círculo.
- El área del círculo se calcula como: A = pi * r^2, donde "r" es el radio del círculo.

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> Radio
**Proceso** -> Dado el Radio de un circulo, lo multiplico por 2π para calcular el perimetro, para calcular el area lo elevo al cuadrado y lo multiplico por π

**Salida** -> mostrar perimetro y area

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo ÁreayPerímetro
	perimetro = 2 * pi * Radio
    area = pi * radio ** 2
```

# Ejercicio 5

### Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor.

**Paso 1**: Definir el problema

El problema consiste en encontrar el número más grande y el número más pequeño de una lista de números enteros. La solución debe ser un algoritmo que recorra la lista de números y compare cada uno de ellos con las variables "mayor" y "menor" para determinar cuál es el número más grande y cuál es el número más pequeño.

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> numeros = lista de numeros
**Proceso** ->  Creo la variable *menor* y *mayor*. Itero por la lista de numeros, en caso de que el numero por el que se este iterando sea mayor a *mayor* o menor a *menor*, lo copio dentro de esa variable

**Salida** -> 
    mayor = numero mayor
    menor = numero menor

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo mayoryMenor
declaro mayor y menor 
 for i in numeros:
    si valor(i) < menor
        menor = valor(i)
    si valor(i) > mayor
        mayor = valor(i) 
```

# Ejercicio 6

## **Crea un algoritmo que convierta grados Celsius a Fahrenheit.**

**Paso 1**: Definir el problema

Nos piden desarrollar un algoritmo que permita convertir una temperatura en grados Celsius a su equivalente en grados Fahrenheit. Se resuelve utilizando una fórmula de conversión `ºF=(ºC*1.8) + 32`.

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> celsius = input(celsius)
**Proceso** -> Dado un valor Celsius de temperatura, lo multiplico por 1.8 y le agrego 32 para conseguir su equivalente en Farenheit

**Salida** -> printear(Farenheit)

**Paso 3**: Escribir el pseudocódigo.

  

`Algoritmo celsiusAFarenheit`

`Farenheit = celsius*1.8 + 32` 


# Ejercicio 7

### Dado un número entero, crea un algoritmo que determine si es par o impar

**Paso 1**: Definir el problema

Para determinar si un número es par o impar debemos calcular su módulo 2 (el resto de la división del número entre 2). Si el resto es igual a cero, el número es par. Si no, es impar.

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> numero = numero ingresado
**Proceso** -> Divido el numero por 2, en caso de que el resto sea 0 el numero es par, caso contrario es impar

**Salida** -> Par == 1 -> Printear par
                    sino printear impar

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo ImparoPar
resto = numero%2
    si resto == 1
        Par = 0
    sino 
        par = 1
```



# Ejercicio 8

### Crea un algoritmo que determine si un año es bisiesto o no.

**Paso 1**: Definir el problema

Un año bisiesto es aquel año que tiene **366 días** en lugar de 365, en el que febrero tiene 29 días en lugar de 28. Se repite **cada cuatro años**, excepto cuando el año acaba en dos ceros.

Condiciones para determinar cuando un año es bisiesto:

- **Debe** se divisible entre 4

- **No debe** ser divisible entre 100.

  Si lo es, el año es bisiesto si:

  - **Es divisible** entre 400. Si no lo es, **no es bisiesto**.

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> año = año ingresado
**Proceso** -> Si el año ingresado es divisible por 400 es biciesto. Si no es divisible por 400 y por 100 pero si lo es por 4, es biciesto. En todos los otros casos no lo es.

**Salida** -> Printear es biciesto si biciesto == 1 sino no es biciesto

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo añoBisiesto
	si año%400 == 0
       	Biciesto = 1
   elseif año%4 == 0 y año%100 != 0
   		biciesto = 1
   else 
        biciesto = 0 
```

# Ejercicio 9

### Crea un algoritmo que determine si una cadena de texto es un palíndromo o no.

**Paso 1**: Definir el problema

Un palindromo es una palabra que se lee igual de derecho que del revés, debemos verificar si la palabra ingresada es un palindromo o no 

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** --> palabra = ingresar texto
**Proceso** -> Utilizo una lista auxiliar donde escribire cada letra de la palabra original pero en orden contrario, empezando por la ultima y terminando en la primera.

Luego comparo cada letra en ambas listas y en caso de que todas las letras sean iguales la palabra es un palindromo.

**Salida** -> si return 1 -> palindromo, sino no es

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo Palindromo
	for i in palabra
                arbalap[i] = palabra[len(palabra) -i]
            for i in arbalap
                if palabra[i] =! arbalap[i]
                    return 0
            return 1
```

# Ejercicio 10

### Dada una lista de nombres, crea un algoritmo que ordene la lista alfabéticamente.

**Paso 1**: Definir el problema:

Lista de nombres separados por comas. Hay que ordenar alfabeticamente los nombres

**Paso 2**: Ingresar la entrada, el proceso y la salida.

***Entrada*** -> lista[1,2,3,4] donde cada numero es un nombre 
**Proceso** -> Primero leo la primer letra de cada nombre y calculo el valor ASCII de ella, luego ordeno las palabras segun el valor de su primer letra.

En caso de que haya 2 letras con el mismo valor repito el procedimiento con la siguiente letra

**Salida** -> print lista ordenada

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo ordenarAlfabeticamenteLista
	lista_ordenada[]
            for i in lista
                leer la primer letra
            si las letras son distintas, escribir en lista_ordenada[] el nombre con la menor letra
            sino leer la segund y loopear
```




# Ejercicio 11

### Crea un algoritmo que calcule el factorial de un número entero.

**Paso 1** : Definir el problema

El factorial de un numero es igual a ese numero multiplicado por todos los valores enteros anteriores a el. Para hacer esto es necesario iterar por todos los valores enteros anteriores al numero seleccionado y multiplicarlos

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> numero = numero ingresado
            Factorial = 1
**Proceso** -> Dado el numero ingresado, se multiplica el numero una vez por cada valor menor a ese numero.

**Salida** -> imprimir factorial

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo calculoFactorial
while(numero > 1): 
	factorial = factorial*numero
	numero -= 1
```

# Ejercicio 12

### Dado un número entero, crea un algoritmo que determine si es primo o no.

**Paso 1**: Definir el problema

Un numero primo es aquel numero que solo es divisible por si mismo y por 1. Debemos comprobar que el resultado de dividir el numero ingresado por cualquier otro numero da un resto =! 0

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> numero = numero ingresado
**Proceso** ->  Solo pueden ser primos los numeros mayores o iguales a 2 por lo que descarto los menores a el, luego declaro el 2 como primo.

Por ultimo calculo el resto de dividir ese numero por todos los valores menores a el, en caso de que el resto sea 0 ese numero no es primo ya que es divisible por un numero distinto a el mismo.

**Salida** -> dice si es primo o no

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo Primo
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




# Ejercicio 13

### Crea un algoritmo que calcule el área y volumen de un cubo dado su lado.

**Paso 1**: Definir el problema

El area de un cubo es igual a un lado del mismo elevado al cuadrado y multiplicado por la cantidad de caras que tiene. El volumen de un cubo es igual al lado del mismo elevado al cubo

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> lado = lado del cubo
**Proceso** -> Una vez dado el lado del cubo se lo potencia al cuadrado y multiplica por 6 para calcular el area y luego el lado se lo potencia al cubo para calcular el volumen

**Salida** -> el area es *area* y el volumen del cubo es *volumen*

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo Cubo
area = 6 * lado^2
volumen = lado ^ 3
```

# Ejercicio 14

### Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista

**Paso 1**: Definir el problema

Primero debemos calcular el modulo2 de cada valor para determinar si el numero es par o no, luego sumaremos el valor de todos aquellos numeros que cumplan esta condicion y devolveremos el total.

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> lista[] = lista de numeros
            total_par = total de numeros par (int)
**Proceso** -> Pido una lista de numeros al usuario.

Divido cada valor de la lista y, en caso de que el resto de ese valor sea 0, sumo ese numero al total_par.

**Salida** -> imprimir total_par

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo sumaPares
	for i in lista[]
        if valor(i)%2 == 0
            total_par = total_par + valor(i)
            i = i+1
        else
            i = i+1
```

# Ejercicio 15

### Crea un algoritmo que determine si un número es positivo, negativo o cero.

**Paso 1**: Definir el problema

El problema consiste en distinguir cuando un número es mayor, menor o igual que cero.

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> numero = numero ingresado
           tipo = tipo de numero (string)
**Proceso** -> Leo el numero ingresado e imprimo al usuario si el numero es mayor, igual o menor a cero

**Salida**-> imprimir tipo

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo determinarSigno
	if numero < 0 
        tipo = "negativo"
    elif numero > 0
        tipo = "positivo"
    else 
        tipo = "0"
```

# Ejercicio 16

### Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista

**Paso 1**: Definir el problema

El problema consiste en, dada una lista de números enteros, calcular la media de los números de la misma.

Para resolver el problema se necesita realizar la **suma de todos los números y dividir el resultado entre la cantidad de valores que tengamos en la lista**.

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> lista[] = lista de numeros
            total = 0
**Proceso** -> Sumo la totalidad de los numeros en la lista y luego los divido por la cantidad de numeros en ella

**Salida** -> imprimir lista

**Paso 3**: Escribir el pseudocódigo.

```
 Algoritmo calcularMediaLista
 for i in lista
        total = total + i
    media = total/len(lista[])
```

# Ejercicio 17

##### Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.

**Paso 1**: Definir el problema

El problema consiste en, dado un rango de números enteros entre 1 y 100, crear un algoritmo que genere un número aleatorio y le pida al usuario adivinarlo. El algoritmo debe indicar si el número introducido por el usuario es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** ->  rng = numero al azar entre 1 y 100
            numero = numero usuario
**Proceso** -> Genero un numero al azar **rng**  y pido al usuario un numero.

Lo leo y le comunico al usuario si el numero es mayor, menor o igual al **rng**, en caso de no ser igual vuelvo a pedir otro numero hasta que sean iguales

**Salida** -> Felicidades, el numero es *rng*

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo AdivinarRng
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

# Ejercicio 18

### Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto.

**Paso 1**: Definir el problema

Determinar si una cadena de texto es un anagrama de otra cadena de texto.

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** ->  palabra1 = palabra original
            palabra2 = palabra a determinar 

si es un anagrama de palabra1
**Proceso** -> Primero creo una lista auxiliar para cada palabra y escribo en ellas las letras de cada palabra pero ordenadas alfabeticamente en lugar de en su orden original.

En caso de que las palabras sean anagramas de la otra, las letras utilizadas seran iguales en ambos casos.

Si ambas listas auxiliares son iguales, las palanras son anagramas

**Salida** -> si anagrama == 1-> las palabras son anagramas, sino no lo son

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo Anagrama
letras1[] = escribir cada letra de palabra1 en una lista y ordenarlas alfabeticamente
    letras2[] = escribir cada letra de palabra2 en una lista y ordenarlas alfabeticamente
    anagrama -> si letras1 == letras 2
            anagrama = 1
        sino
            anagrama = 0
```



# Ejercicio 19

### Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista.

**Paso 1**: Definir el problema

El problema consiste en escribir un programa que a partir de una lista de números enteros como entrada por el usuario y que elimine todos los elementos de la lista que aparezcan más de una vez. Cada número entero aparecerá de esta forma únicamente una vez en la lista numeros2

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** -> numeros[] = cadena de numeros
**Proceso** -> Luego de pedir una cadena de numeros, creo una cadena auxiliar numeros2.

Por cada numero de la cadena original veo los valores de la segunda cadena y, en caso de no estar en ella, lo escribo en numeros2, luego paso al siguiente numero.

Una vez se termine de iterar la lista original imprimo la lista numeros2

**Salida** -> imprime en pantalla *numeros2[]

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo eliminarNumerosDuplicados
numeros2[] = for i in numeros 
	si valor(i) no esta en numeros2[]
		escribirlo
		i = i+1
	sino
		i = i+1
```

# Ejercicio 20 

### Crea un algoritmo que determine si un número es capicúa o no.

**Paso 1**: Definir el problema

El problema consiste en determinar una forma de saber si un numero introducido por el usuario **es igual leído de izquierda a derecha que de derecha a izquierda**.

**Paso 2**: Ingresar la entrada, el proceso y la salida.

**Entrada** ->  numero = numero a ingresar
            numero_inverso[] = lista
**Proceso** -> Primero escribo cada digito del numero original en una lista en orden.

​					Luego creo una nueva lista numero_inverso donde escribo cada digito en orden contrario, iniciando por el ultimo hasta llegar al primero

Al finalizar comparo ambas listas y si son iguales el numero es capicúa

**Salida** -> indica si el numero es capicua   

**Paso 3**: Escribir el pseudocódigo.

```
Algoritmo numeroEsCapicua
nuevo_numero[] = escribir cada digito del numero en un valor de la lista
    for i in nuevo_numero[]
        numero_inverso[i] = nuevo_numero[len(nuevo_numero) - i]
    si numero inverso[] es igual a nuevo_numero[], el numero es capicua 
```
