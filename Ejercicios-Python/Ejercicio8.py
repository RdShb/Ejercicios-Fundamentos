año = input("Inserte un año: ")
if int(año)%400 == 0:
    print("El año es biciesto!")
elif int(año)%4 == 0 and int(año)%100 != 0:
    print("El año es biciesto!")
else:
    print("El año no es biciesto!")







