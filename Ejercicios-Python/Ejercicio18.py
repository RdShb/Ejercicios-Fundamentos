a = input("Escriba una palabra: ")
b = input("Escriba otra palabra: ")
if sorted(a) == sorted(b):
    print("Son anagramas!")
else:
    print("No son anagramas!")