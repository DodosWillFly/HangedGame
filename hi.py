import random
#The variable paraules holds a list of words such as “cat,” “car,” “table,” “book,” and others. These words will likely be used later in the program.
paraules = [
    "gat", "cotxe", "taula", "llibre", "ordinador", 
    "televisor", "casa", "arbre", "mar", "muntanya", 
    "sol", "pluja", "cel", "aire", "terra", 
    "pantalons", "camisa", "pantaló", "aventura", "emoció"
]
paraula = random.choice(paraules)
paraula_oculta = "_" * len(paraula)
nIntents = 5
lletras_encertades = set()


def ComprovarLletra(lletra, paraula):
    lletra = lletra.lower()
    if lletra in paraula.lower():
        lletras_encertades.add(lletra)
        return True
    return False

def ComVaLaParaula(paraula, lletras_encertades):
    paraula_oculta = ""
    for lletra in paraula:
        if lletra.lower() in lletras_encertades:
            paraula_oculta += lletra + " "
        else:
            paraula_oculta += "_ "
    return paraula_oculta.strip()
# The program types welcome to the game and how many characters the secret word has
print("BEN VINGUT AL JOC DE L'AHORCADO O COM ES DIGUI:")
print(f"LA PARAULA OCULTA CONTÉ {len(paraula)} paraules")
print(ComVaLaParaula(paraula, lletras_encertades))

while nIntents > 0 and "_" in paraula_oculta:
    intent = input("Entra una lletra o la paraula sencera: ")
    if len(intent) == 1:
        if ComprovarLletra(intent, paraula):
            print("HAS ENCERTAT")
            paraula_oculta = ComVaLaParaula(paraula, lletras_encertades)
            print(paraula_oculta)
        else:
            nIntents -= 1
            print("F")
            print(f"Tens {nIntents} intents restants.")
            print("SEGÜENT INTENT:")
    else:
        if intent.lower() == paraula.lower():
            paraula_oculta = paraula
        else:
            nIntents -= 1
            print("F")
            print(f"Tens {nIntents} intents restants.")
            print("SEGÜENT INTENT:")
# In case we figure the correct word the program says that you won, else it says the number of trys
# and what the correct word was
if "_" not in paraula_oculta:
    print("Felicitats! Has encertat la paraula.")
else:
    print("Has superat el nombre d'intents disponibles. La paraula era:", paraula)
