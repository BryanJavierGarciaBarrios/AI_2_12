import sympy

# Variables proposicionales
A, B, C = sympy.symbols('A B C')

# Fórmulas
formula1 = (~A | B | C)  # ¬A ∨ B ∨ C
formula2 = (A | ~B | C)   # A ∨ ¬B ∨ C
formula3 = (A | B | ~C)   # A ∨ B ∨ ¬C

# Crear una lista de fórmulas en forma normal conjuntiva (CNF)
cnf = sympy.to_cnf(formula1 & formula2 & formula3)

# Realizar resolución
result = sympy.satisfiable(cnf)

if result:
    print("La fórmula es satisfactible.")
    model = dict(result)
    print("Modelo de satisfacción:")
    print(model)
else:
    print("La fórmula no es satisfactible.")
