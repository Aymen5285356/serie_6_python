chaine = input("Entrez une chaîne de caractères : ")
compteur = {}
for lettre in chaine:
    if lettre != ' ':
        if lettre in compteur:
            compteur[lettre] += 1
        else:
            compteur[lettre] = 1
print(compteur)
