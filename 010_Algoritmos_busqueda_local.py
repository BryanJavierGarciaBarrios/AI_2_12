import random

# Ejemplo de fórmula CNF
cnf_formula = [[1, 2, -3], [-1, 2, 3], [1, -2, 3], [-1, -2, -3]]

# Función para evaluar una asignación de verdad en la fórmula
def evaluate_assignment(assignment, formula):
    for clause in formula:
        clause_satisfied = any(literal in assignment for literal in clause)
        if not clause_satisfied:
            return False
    return True

# Algoritmo de búsqueda local para la satisfacción de CNF
def local_search(cnf_formula, max_iterations=1000):
    num_variables = max(max(map(abs, clause)) for clause in cnf_formula)
    current_assignment = [random.choice([True, False]) for _ in range(num_variables)]

    for _ in range(max_iterations):
        unsatisfied_clauses = []

        for i, clause in enumerate(cnf_formula):
            clause_satisfied = any(literal in current_assignment for literal in clause)
            if not clause_satisfied:
                unsatisfied_clauses.append(i)

        if not unsatisfied_clauses:
            return current_assignment  # Se encontró una solución

        random_clause = random.choice(unsatisfied_clauses)
        random_literal = random.choice(cnf_formula[random_clause])

        # Cambiar el valor del literal en la asignación
        current_assignment[abs(random_literal) - 1] = not current_assignment[abs(random_literal) - 1]

    return None  # No se encontró una solución en el número máximo de iteraciones

# Ejecutar la búsqueda local
solution = local_search(cnf_formula)

if solution:
    print("Se encontró una solución: ", solution)
    print("La fórmula es satisfacible.")
else:
    print("No se encontró una solución en el número máximo de iteraciones.")
    print("La fórmula no es satisfacible.")
