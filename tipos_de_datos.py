""" String : los string son la representacion de texto esto se logra al encerrar la cadena de caracteres entre "" o '' lo q le dice a python que lo que esta dentro de eso es un texto para saber cuando usar "" o '' para un string
si el documento en el que estamos trabajando esta usando "" usaremos '' para los strings y al revez 
si el documento que estamos utilizando contiene '' usaremos "" para los strings
si quieres que al momento de imprimir un string aparescan "" o '' debes encerrarlo primero con las otras comillas 
si necesitas escribir un texto que contenga saltos de linea puedes escribirlo con triple comillas dobles o triple comillas simple dentro de una variable, python reconocera esto como un string y no como un comentario
"""
cadena = "Hola mundo" + ' esto es un string en comillas simples'
ejemplo_1 = '"hola mundo"'
ejemplo_2 = "'Hola mundo'"
comillas_triples = """ Esto es un texto
escrito en triple comillas dobles
con saltos de linea"""

print(ejemplo_1, ejemplo_2,comillas_triples)

"""int o integer es la representacion de un numero entero en python para que python lo reconosca como un numero entero no debe estar encerrado entre "" o '' ni debe tener un pounto al final de este, si agregas una coma el sistema reconocera el numero despues de la coma como un numero nuevo y no como un decimal tambien puede reconocer al numero negativo
al dividir con / nos entregara un resultado de tipo float
al dividir con // nos entregara un dato de tipo int 
estos operadores aritmeticos pueden ser usados tanto para los datos tipo int y float
"""


entero = 1

entero_negativo = -1,-2,-3,-4
dividir_entero = 10//3 
dividir_flotante = 10/5
print(dividir_entero, dividir_flotante)

#el float es la representacion de un numero real o decimal este no debe estar encerrado entre "" o ''
flotante = 1.3

Booleano = 1 < 0 #esta es la representacion de un tipo de dato cuya respuesta sera True o False


#tambien se puede saber que tipo de dato estas usando el comando type(dentro del parentesis colocas el dato que quieres saber)

print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(Booleano))