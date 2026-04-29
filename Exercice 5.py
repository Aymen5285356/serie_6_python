def comptage(mot):
    dico = {}
    for caractere in mot:
        if caractere.isalpha() and caractere.isupper():
            if caractere in dico:
                dico[caractere] += 1
            else:
                dico[caractere] = 1
    return dico