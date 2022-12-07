menu = "1. Introdueix una frase \n2. Elimina les vocals \n3. Elimina les consonants " \
       "\n4. Ordena la frase al revés i printala per pantalla " \
       "\n5. Ordena les paraules de la frase en orde ascendent i printales per pantalla"


def insertaFrase():
       frase = input("Inserta una frase")
       return frase

def eliminaVocales(frase):
       vocales = "aeiou"
       nFrase = ""
       for letra in frase:
              if not letra.lower() in vocales:
                     nFrase += letra
       return nFrase

def ordenaReves(frase):
       nFrase = ""
       for letra in range(0, len(frase), -1):
              nFrase += frase[letra]
       return nFrase


frase = insertaFrase()
print(eliminaVocales(frase))






