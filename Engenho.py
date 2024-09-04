# MODEL:

# regras = [
#     {"se": ["F", "B"], "entao": "Z"},
#     {"se": ["C", "D"], "entao": "F"},
#     {"se": ["A"],      "entao": "D"},
# ]

# fatos = {"A", "B", "C"}

# meta = "Z"

def foward_chaining(rules, initFacts, goal=None):
    facts = initFacts.copy()
    while True:
        newFact = False
        for rule in rules:
            if all(fact in facts for fact in rule["se"]):
                if rule["entao"] not in facts:
                    facts.add(rule["entao"])
                    newFact = True
        if not newFact:
            break
    if(goal):
        return True
    return facts


def backward_chaining(rules, facts, goal):
    # Se a meta já é um fato conhecido, retornamos True
    if goal in facts:
        return True
    
    # Procura por regras que possam inferir a meta
    for rule in rules:
        if rule["entao"] == goal:
            # Verifica se todos os antecedentes da regra são verdadeiros
            if all(backward_chaining(rules, facts, subgoal) for subgoal in rule["se"]):
                return True
    
    # Se não conseguir inferir a meta, retorna False
    return False


def mixed_chaining(rules, facts, goal):
    # Se a meta já é um fato conhecido, retornamos True
    if goal in facts:
        return True

    # Procura por regras que possam inferir a meta
    for rule in rules:
        if rule["entao"] == goal:
            facts = foward_chaining(rules, facts);
            # Verifica se todos os antecedentes da regra são verdadeiros
            if all(backward_chaining(rules, facts, subgoal) for subgoal in rule["se"]):
                return True
    
    # Se não conseguir inferir a meta, retorna False
    return False