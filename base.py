import Engenho, Regras;

fatos = {"A", "B", "C", "F"}

meta = "H"

print(Engenho.backward_chaining(Regras.regras, fatos, meta))