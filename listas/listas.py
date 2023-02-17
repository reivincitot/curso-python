#----------------------------------------Video 2 Listas-----------------------------------------------------------

#indices         [0]        [1]       [2]     [3]     [4] 
#indeices negativos [-5]    [-4]      [-3]    [-2]    [-1]
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

# primer_curso = lista_cursos[0]
# print(primer_curso)

# segundo_curso = lista_cursos[1]
# print(segundo_curso)

# tercer_curso = lista_cursos[2]
# print(tercer_curso)

# cuarto_curso = lista_cursos[3]
# print(cuarto_curso)

# ultimo_curso = lista_cursos[-1] #python permite leer desde el final de la lista si colocas el signo - mas el numero del elemento que buscas, como ejemplo para obtener el ultimo indicen
#                                 #en vez de colocar el numero [4] para obtener el ultimo curso se escribio [-1]
# print(ultimo_curso)

#---------------------------------------------Video 3 Actualizar Elementos----------------------------------------------

lista_cursos[4] = 'Rust' #para actualizar un objeto de la lista solo debes llamar a la lista junto con el indice del objeto que deseas modificar seguido de un signo igual y el nuevo objeto
print(lista_cursos)