"""print("Hola git test")

#Ejercicio 1

while True:

    celcius = int(input("Ingrese una temperatura en Celcius: "))
    if celcius is not int:
        print("Ingrese un número")

farenheit = (celcius*9/5)+32
print(f"{celcius}.0°C equivale a {farenheit}.0°F")

#Ejercicio 2

while True:

    largo = int(input("Ingrese el largo del rectángulo: "))
    if largo is not int:
        print("Ingrese un número")
    else: ancho = int(input("Ingrese el ancho: "))
    if ancho is not int:
        print("Debe ser un número")

area = (largo*ancho)
perimetro = (2*(largo+ancho))
print(f"Largo:{largo}\nAncho: {ancho}\nArea: {area}\nPerimetro: {perimetro}")"""

#Ejercicio 3

anionacimiento= int(input("Ingrese su año de nacimiento: "))
anioactual= int(input("Ingrese el año actual: "))

edadactual= anioactual - anionacimiento
edad2050= 2050 - anionacimiento
print(f"Tu edad actual es {edadactual} y tu edad en 2050 será {edad2050}")

#Ejercicio 4

