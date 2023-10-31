from pyknow import Fact, KnowledgeEngine, Rule

class KnowledgeBase(KnowledgeEngine):
    @Rule(Fact(action="help"))
    def help(self):
        print("La base de conocimiento en lógica proposicional permite representar afirmaciones y realizar inferencias lógicas.")
        print("Puedes agregar hechos y reglas, y hacer consultas para obtener conclusiones basadas en la lógica proposicional.")
        self.declare(Fact(action="finished"))

    @Rule(Fact(action="declare_fact"))
    def declare_fact(self, fact_text):
        self.declare(Fact(fact=fact_text))
        print(f"Se ha declarado el hecho: {fact_text}")

    @Rule(Fact(action="declare_rule"))
    def declare_rule(self, rule_text):
        self.declare(Rule(rule=rule_text))
        print(f"Se ha declarado la regla: {rule_text}")

    @Rule(Fact(action="query"))
    def query(self):
        for fact in self.facts:
            if fact.asserted:
                print(f"Hecho: {fact['fact']}")
        self.declare(Fact(action="finished"))

if __name__ == '__main__':
    kb = KnowledgeBase()
    kb.reset()

    print("Ejemplo de base de conocimiento en lógica proposicional con PyKnow")
    print("Puedes realizar las siguientes acciones:")
    print("1. Declarar un hecho (Ejemplo: declare_fact('P and Q'))")
    print("2. Declarar una regla (Ejemplo: declare_rule('R: (P and Q) => S'))")
    print("3. Consultar los hechos declarados (Ejemplo: query())")
    print("4. Obtener ayuda (Ejemplo: help())")
    print("5. Salir (Ejemplo: exit())")

    while True:
        action = input("Ingrese una acción: ")
        try:
            kb.reset()
            kb.declare(Fact(action=action))
            kb.run()
        except SystemExit:
            break
