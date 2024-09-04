import Engenho

regras = [
    {"se": ["A", "B"],      "entao": "C"},
    {"se": ["A"],           "entao": "D"},
    {"se": ["C", "D"],      "entao": "E"},
    {"se": ["B", "E", "F"], "entao": "G"},
    {"se": ["A", "E"],      "entao": "H"},
    {"se": ["D", "E", "H"], "entao": "I"},
]

regrasInf = [
    # Modus Ponens
    {"se": ["P"],                "entao": "Q"},
    # Modus Tollens
    {"se": ["~Q"],               "entao": "~P"},
    # Silogismo Hipotético
    {"se": ["P -> Q", "Q -> R"], "entao": "P -> R"},
    # Silogismo Disjuntivo
    {"se": ["~P"],               "entao": "Q"},
    # Introdução do &
    {"se": ["P", "Q"],           "entao": "P & Q"}
]

fatos = {"A", "B", "F"}

meta = "H"