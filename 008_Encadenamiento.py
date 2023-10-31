class Rule:
    def __init__(self, premise, conclusion):
        self.premise = premise
        self.conclusion = conclusion

    def apply(self, facts):
        # Comprueba si la premisa de la regla es verdadera
        if all(p in facts for p in self.premise):
            return self.conclusion
        else:
            return None

class ForwardChaining:
    def __init__(self, rules):
        self.rules = rules

    def forward_chain(self, initial_facts):
        facts = set(initial_facts)
        new_facts = set()

        while True:
            found_new_fact = False
            for rule in self.rules:
                conclusion = rule.apply(facts)
                if conclusion is not None and conclusion not in facts:
                    new_facts.add(conclusion)
                    found_new_fact = True

            if not found_new_fact:
                break

            facts.update(new_facts)

        return facts

# Definición de reglas y hechos iniciales
rules = [
    Rule({'A', 'B'}, 'C'),
    Rule({'C'}, 'D'),
    Rule({'E'}, 'F'),
]

initial_facts = {'A', 'B', 'E'}

# Realizar encadenamiento hacia adelante
engine = ForwardChaining(rules)
inferred_facts = engine.forward_chain(initial_facts)

print("Hechos iniciales:", initial_facts)
print("Hechos inferidos:", inferred_facts)
