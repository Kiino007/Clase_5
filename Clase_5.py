#Funciones de programacion


#En esta sesion aprenderemos:

#Que es una funcion 
#Como se estructuran las funciones en un lenguaje de programacion
#Cuales son los beneficios de utilizar funciones en nuestros programas
#Como funcionan los parametros y el retorno de valores (Sin aplicarlo en codigo todavia)
#Ejemplos y ejercicios practicos para comprender la logica detras del uso de funciones


#Que es una funcion en programacion?
#Una funcion es un bloque de codigo que tiene un proposito especifico dentro de un programa. se usa para 
#dividir el codigo en partes mas pequeñas y reusables, lo que hace que los programas sean mucho mas 
#organizados y faciles de enetender


#Imagina que quieres preparar una pizza en casa. en lugar de hacer todo el proceso cada vez que la cocinas, 
#podrias tener pasos organizados

#preparar la masa
#agregar los ingredientes
#hornear la pizza
#servir 

#cada uno de estos pasos es una funcion dentro del proceso general de hacer una pizza. cuando quieras hacer 
#otra pizza, simplemente sigues los mismos pasos en orden, sin necesidad de inventar un nuevo proceso desde cero


#como funciona...

#para entender como funciona una funcion, debemos pensar en 3 aspectos clave

#1 Definicion de la funcion: Se establece el bloque de codigo con un nombre que lo identifica 

#2 Invocacion de la funcion: Se ejecuta la funcion cuando es necesario dentro del programa 

arreglo = []
numero = len(arreglo)

#Retorno de valores: Una funcion puede resolver un resultado para ser usado en alguna parte del codigo (return)

#beneficios:
#reusar codigo
#En lugar de escribir el codigo varias veces, escribo eso una sola vez y la llamo cuando la necesite

#Organizacion y modular
#dividir un programa en funciones hace que el codigo sea mas estructurado y facil de entender 

#3 Facilidad del mantenimiento
#si hay errores en la ejecucion, se puden corregir en una sola funcion, en lugar de buscar varias partes del programa 

#Escalabilidad
#Se puede agrandar el enfazis o alcance del proyecto con menos codigo, manejando mas cosas con el menor esfuerzo.....
#Contruir programas mas grandes de una manera mas ordenada y logica

#Facilita el trabajo en equipo
# en proyectos grandes los devs pueden trabajar en funciones separadas sin afectar otras partes del codigo

#Componentes de una funcion

#nombre de la funcion:
#identificador unico que permite llamarla cuando sea necesario

#Parametros(opcional):
#Son los datos que recibe una funcion para trabajar con ellos 

#Cuerpo de la funcion
#Es un bloque de codigo que define el comportamiento de la funcion 

#valor de retorno(opcional):
#resultado que a funcion va a devolver al flujo principal

#diferencia entre una funcion y un bloque de codigo



# //////////////////////////////////////////////////////////////////////

#Ejemplo en pseudocodigo de como calcular el area de un rectangulo

#1 pedir la base y la altura
#2 multiplicar base * altura
#3 mostrar el resultado


#parametros y retornos
#las funciones reciben parametros que devuelven resultados

#parametro: es el insumo con el que trabaja la funcion

#retorno: es el resultado de procesar los parametros

#1. ingresar "Late" y "grande" como parametros a la maquina 
#2 la maquina prepara el cafe
#3 la maquina devuelve el cafe listo

# sin funciones

edad = int(input("ingrese su edad: "))

if edad >= 18:
    print("eres mayor de edad")

else:
    print("te redirijo a google")

#con funcion
def verificar_edad(edad):
    if edad >= 18:
        print("eres mayor de edad")

    else:
        print("te redirijo a google")

edad_usuario = int(input("Ingrese su edad"))
verificar_edad(edad_usuario)