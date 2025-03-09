# FUNDAMENTOS-DE-PROGRAMACION
CREACIÓN DE UN REPOSITORIO EN GITHUB.

UNIVERSIDAD ESTATAL AMAZONICA.  

CARRERA: TECNOLOGIAS DE LA INFORMACIÓN. 

ASHLEY SCARLET ALVARADO PILOZO.

#Uso de la estructura if-else
numero = int(input("Ingresa un numero: "))
resto = numero%4

if resto==0:
    print("El numero es par")
else:
    print("El numero es impar")

print("Fin")

#Ejemplo 

nota = 50

if nota >= 90:
    print("Tu calificación es A, felicidades")
elif nota >= 80:
    if nota >= 85:
        print("Tu calificación es B+, exelente.")
    else:
        print("Tu calificación es B, exelente.")
elif nota >= 70:
    print("Tu calificación es C.")
elif nota >= 60:
    print("Tu calificación es D.")
else:
    print("Tu calificación es F, reprobaste.")
