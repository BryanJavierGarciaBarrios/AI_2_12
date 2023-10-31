import itertools

# Función para evaluar una expresión lógica y construir su tabla de verdad
def tabla_de_verdad(expresion):
    variables = set([c for c in expresion if c.isalpha()])
    combinaciones = list(itertools.product([False, True], repeat=len(variables)))
    tabla = []

    for combinacion in combinaciones:
        valores = dict(zip(variables, combinacion))
        resultado = eval(expresion, valores)
        fila = {**valores, 'Resultado': resultado}
        tabla.append(fila)

    return tabla

# Función para verificar si dos expresiones lógicas son equivalentes
def son_equivalentes(expresion1, expresion2):
    tabla1 = tabla_de_verdad(expresion1)
    tabla2 = tabla_de_verdad(expresion2)

    return tabla1 == tabla2

# Expresiones a comparar
expresion1 = "(A and B) or (not A and not B)"
expresion2 = "not (A or B) and (not A or not B)"

# Verificar si son equivalentes
if son_equivalentes(expresion1, expresion2):
    print(f"Las expresiones son equivalentes.")
else:
    print(f"Las expresiones no son equivalentes.")
