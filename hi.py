import random
#The variable paraules holds a list of words. These words will likely be used later in the program.
paraules = [
    "gat", "cotxe", "taula", "llibre", "ordinador", 
    "televisor", "casa", "arbre", "mar", "muntanya", 
    "sol", "pluja", "cel", "aire", "terra", 
    "pantalons", "camisa", "pantaló", "aventura", "emoció"
]
# Initializating
paraula = random.choice(paraules)
paraula_oculta = "_" * len(paraula)
nIntents = 5
lletras_encertades = set()
#This function checks if a guessed letter is present in the chosen word
#It converts the letter to lowercase and checks if it exists in the word (ignoring case)
#If the letter is correct, it’s added to the lletras_encertades set, and True is returned. Otherwise, False is returned


def ComprovarLletra(lletra, paraula):
    lletra = lletra.lower()
    if lletra in paraula.lower():
        lletras_encertades.add(lletra)
        return True
    return False
#This function constructs the partially revealed word based on correctly guessed letters
#It iterates through each letter in the original word
#If the letter is in lletras_encertades, it’s revealed. Otherwise, an underscore is displayed.
#The result is returned as a string without extra spaces

def ComVaLaParaula(paraula, lletras_encertades):
    paraula_oculta = ""
    for lletra in paraula:
        if lletra.lower() in lletras_encertades:
            paraula_oculta += lletra + " "
        else:
            paraula_oculta += "_ "
    return paraula_oculta.strip()

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
