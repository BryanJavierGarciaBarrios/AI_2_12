import itertools

# Definición de funciones para la lógica proposicional

def parse_propositional_logic(expression):
    # Esta función analiza una expresión lógica proposicional y devuelve una representación estructurada.
    # Puedes personalizar esta función según tus necesidades.

    # En este ejemplo, asumiremos que la expresión lógica está en forma de cadena y contiene operadores binarios como "&" (AND) y "|" (OR).

    # Reemplaza los operadores lógicos por versiones de Python
    expression = expression.replace("&", "and").replace("|", "or")

    # Evaluar la expresión y devolver el resultado
    result = eval(expression)
    return result

def is_valid_argument(propositions, conclusion):
    # Esta función verifica la validez de un argumento en lógica proposicional.
    # propositions es una lista de proposiciones y conclusion es la conclusión que se debe verificar.

    for values in itertools.product([True, False], repeat=len(propositions)):
        assignment = dict(zip(propositions, values))
        if not parse_propositional_logic(conclusion).subs(assignment):
            return False

    return True

# Ejemplo de argumento
propositions = ["p", "q"]
conclusion = "(p & q) | (p & ~q) | (~p & q)"

if is_valid_argument(propositions, conclusion):
    print("El argumento es válido.")
else:
    print("El argumento no es válido.")
