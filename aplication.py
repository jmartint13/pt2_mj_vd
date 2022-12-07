menu = "1. Introdueix una frase \n2. Elimina les vocals \n3. Elimina les consonants " \
       "\n4. Ordena la frase al revés i printala per pantalla " \
       "\n5. Ordena les paraules de la frase en orde ascendent i printales per pantalla"



def eliminarcons(frase):
       voc = "aiueo"
       resultado = ""
       for i in frase:
              if i in voc or i == " " or i.isdigit():
                     resultado += i
       return resultado


