import sys

numeros = int(input("Introduzca los numeros de su DNI: "))
letrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"

numletra = numeros % 23
letra = letrasDNI[numletra]
print(f"Su DNI es: {numeros}{letra}")
