dico_fr_en = {
    "bonjour": "hello",
    "merci": "thank you",
    "au revoir": "goodbye",
    "oui": "yes",
    "non": "no",
    "maison": "house",
    "voiture": "car",
    "chat": "cat",
    "chien": "dog",
    "soleil": "sun",
    "lune": "moon",
    "eau": "water",
    "pain": "bread",
    "fromage": "cheese",
    "vin": "wine",
    "livre": "book",
    "ecole": "school",
    "professeur": "teacher",
    "etudiant": "student",
    "ordinateur": "computer"
}
def traduction(mot_fr):
    return dico_fr_en.get(mot_fr, None)
mot = input("Entrez un mot en français : ")
traduction_mot = traduction(mot)
if traduction_mot:
    print(f"Traduction : {traduction_mot}")
else:
    reponse = input("Le mot n'existe pas. Voulez-vous l'ajouter ? (oui/non) : ")
    if reponse.lower() == "oui":
        anglais = input("Entrez la traduction anglaise : ")
        dico_fr_en[mot] = anglais
        print("Mot ajouté avec succès !")