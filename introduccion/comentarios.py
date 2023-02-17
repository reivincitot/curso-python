import string
import random


chars = string.ascii_uppercase + string.digits
letters = ''.join(random.choice(chars) for _ in range(10))

print (letters)
#esto es un comentario
print('esto no es un comentario con #')

"""esto es un comentario tambien, este tipo de comentario se usa para poder detallar informacion en multiples lineas al contrario del # que solo comenta una sola linea"""
print("esto es un comentario con triple comillas dobles ")