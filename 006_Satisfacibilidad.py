import pycosat

# Función para verificar la satisfacibilidad de una expresión lógica
def verificar_satisfacibilidad(expresion):
    cnf = []  # Forma normal conjuntiva (CNF) de la expresión

    # Supongamos que la expresión está en forma de una cadena
    # Ejemplo: (A or B) and (not A or C)
    clausulas = expresion.split("and")
    
    for clausula in clausulas:
        variables = clausula.split("or")
        clausula_cnf = [int(v) for v in variables]
        cnf.append(clausula_cnf)
    
    try:
        resultado = pycosat.solve(cnf)
        if resultado is not None:
            return True, resultado
        else:
            return False, None
    except pycosat.SolveFailed:
        return False, None

# Ejemplo de expresión lógica para verificar satisfacibilidad
expresion = "(A or B) and (not A or C)"

satisfacible, asignacion = verificar_satisfacibilidad(expresion)

if satisfacible:
    print(f"La expresión es satisfacible. Asignación de valores de verdad:")
    print(asignacion)
else:
    print("La expresión no es satisfacible.")
