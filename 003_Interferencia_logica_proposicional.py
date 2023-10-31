from sympy import symbols, Implies, Not, And, Or, simplify_logic

# Definir símbolos proposicionales
p, q, r = symbols('p q r')

# Definir proposiciones
proposition_1 = Implies(p, q)  # p implica q
proposition_2 = Or(Not(p), r)  # No p o r
proposition_3 = And(proposition_1, proposition_2)  # (p implica q) y (no p o r)

# Simplificar la proposición
simplified_proposition = simplify_logic(proposition_3)

# Comprobar la inferencia
if simplified_proposition == True:
    print("La proposición 3 implica True.")
else:
    print("La proposición 3 no implica True.")
