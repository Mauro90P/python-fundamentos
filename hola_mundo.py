# 1. TAREA: imprime "Hola, mundo"
print("Hola, mundo")
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Mauricio"
last_name = "Pardo"
print("Hola", name, last_name)  # con una coma
print("Hola " + name + last_name)  # con un +
# 3. imprimir "Hola 42!" con el número en una variable

name = 33
print("Hola", name)  # con una coma
print("Hola " + str(name))  # con una +	-- este debería arrojar un error!

# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "completo"
fave_food2 = "churrasco"
print("Amo comer {} y {} son super ricos.".format(
    fave_food1, fave_food2))  # con .format()
# con una cadena f
print(f"Amo comer {fave_food1} y {fave_food2} son super ricos")

movie1 = "Rapido y furioso"
movie2 = "Ninja gaiden"
print(f"Me encanta la pelicula {movie1} y tambien {movie2} son excelente.")
