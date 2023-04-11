año = int(input("Inserte un año: "))
if año%400 == 0:
    biciesto =("El año es biciesto!")
elif año%4 == 0 and año%100 != 0:
    biciesto =("El año es biciesto!")
else:
    biciesto =("El año no es biciesto!")
print(biciesto)






