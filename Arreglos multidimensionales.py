#Explorando Estructuras de Bucle en Python
#Bucle for

# Iniciamos con una variable para almacenar la suma
suma = 0

# Usamos un bucle for para iterar sobre los primeros 10 números enteros positivos
for i in range(1, 11):  # range(1, 11) genera los números del 1 al 10
    suma += i  # Sumamos el valor de i a la variable suma

# Obtenemos el resultado
print(f"La suma de los primeros 10 números enteros positivos es: {suma}")