#!/usr/bin/env python3

"""
Petit interpréteur en ligne de commande permettant d’appliquer des transformations simples
sur du texte.

L’utilisateur saisit une commande suivie d’un argument, et le programme renvoie le texte
modifié. Les commandes disponibles sont notamment :
- uppercase <texte>  : convertit le texte en majuscules
- lowercase <texte>  : convertit le texte en minuscules
- count-words <texte> : renvoie le nombre de mots
- length <texte>      : renvoie le nombre de caractères
- prefix <texte>      : renvoie les 10 premiers caractères

Le programme boucle de manière interactive jusqu’à la réception d’un EOF (Ctrl+D / Ctrl+Z),
et gère les erreurs basiques (commande inconnue, absence d’argument).
"""

def process_line(line):
    """
    Ça analyse une ligne de commande et ça applique la transformation demandée.
    line est une chaîne contenant "commande texte"
    Ça retourne le résultat de la commande, ou un message d’erreur.
    """
      
    if " " not in line:
        return "No command or no argument given"

    cmd, text = line.split(" ", maxsplit=1)

    if cmd == "uppercase":
        return text.upper()

    if cmd == "lowercase":
        return text.lower()
    if cmd == "length":
        return str(len(text))

    if cmd == "count-words":
        return str(len(text.split()))

    return "Unknown command " + cmd



def main():
    while True:
        try:
            line = input("commade> ")
        except EOFError:
            break

        print(process_line(line))



if __name__ == "__main__":
    main()
