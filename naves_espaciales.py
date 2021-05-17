suma = 0 # Se crea la variable donde se guardaran los números que sean múltiplos de 3 o 5.
for it in range(1000): # Iterador que va de 0 a 999 
    if (it % 3 == 0 or it % 5 == 0):  # Condición que sólo admite los valores que sean múltiplos de 3 o 5
        suma = suma + it  # Se agregan los valores que sean múltiplos a la variable suma


print('The sum of all the multiples of 3 or 5 below 1000 is =', suma) 

import pandas as pd #Para este ejercicio se ocupara la librería de Pandas y sus funciones en cuanto a fechas y tiempo.

inicio = "1901-1-1" # Fecha de inicio del siglo 20
fin    = "2000-12-31" # Fecha de fin de siglo 20


lista_fechas = pd.Series(pd.date_range(start = inicio, end = fin , freq="d")) # pd.Series da formato de una serie de datos 
# pd.data_range crea una serie de datos en formato datetime desde una fecha de inicio hasta una fecha final que
# debe ser colocada por el usuario. freq="d" hace referencia a que nos interesa saber las fechas que hay desde el 
# inicio al final día por día. Esta frecuencia puede ser cambiada dependiendo el rango de interes del usuario.

#lista_fechas = pd.DataFrame(pd.Series(pd.date_range(start = inicio, end = fin , freq="d")))
#lista_fechas.columns = ['date']

primero = lista_fechas[(lista_fechas.dt.day_name() == "Sunday") & (lista_fechas.dt.day == 1)] # En esta línea
# de código se obtienen las fechas que coincidan con la condición de que el día sea domingo y corresponda al 
# primer día del mes. El comando "dt" nos permite acceder a el día, mes o año de una variable en formato datetime.

print("There are",primero.shape[0], "Sundays that fell on the first of the month during the twentieth century")