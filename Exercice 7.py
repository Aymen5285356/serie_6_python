classe = []
def valider_note(note):
    return 0 <= note <= 20
for i in range(10):
    nom = input(f"Nom complet du stagiaire {i+1} : ")
    genre = input("Genre (H/F) : ")
    cc = []
    for j in range(3):
        note = float(input(f"Note CC{j+1} : "))
        while not valider_note(note):
            note = float(input(f"Note invalide. Entrez CC{j+1} (0-20) : "))
        cc.append(note)
    efm = float(input("Note EFM : "))
    while not valider_note(efm):
        efm = float(input("Note EFM invalide. Entrez (0-20) : "))
    classe.append({"nomComplet": nom, "genre": genre, "CC": cc, "EFM": efm})
def calculer_moyenne(stagiaire):
    moyenne_cc = sum(stagiaire["CC"]) / len(stagiaire["CC"])
    moyenne = (moyenne_cc + stagiaire["EFM"]) / 2
    stagiaire["moyenne"] = moyenne
    return moyenne
for stagiaire in classe:
    calculer_moyenne(stagiaire)
def moyenne_generale(classe):
    somme = sum(stagiaire["moyenne"] for stagiaire in classe)
    return somme / len(classe)
def afficher_resultats(classe):
    valides = 0
    for stagiaire in classe:
        statut = "Validé" if stagiaire["moyenne"] >= 10 else "Non Validé"
        print(f"{stagiaire['nomComplet']} : {stagiaire['moyenne']:.2f} - {statut}")
        if statut == "Validé":
            valides += 1
    pourcentage = (valides / len(classe)) * 100
    print(f"Pourcentage de réussite : {pourcentage:.2f}%")
hommes_classe = [s for s in classe if s["genre"] == "H"]
femmes_classe = [s for s in classe if s["genre"] == "F"]
meilleurs_hommes = sorted(hommes_classe, key=lambda x: x["moyenne"], reverse=True)[:2]
meilleure_femme = sorted(femmes_classe, key=lambda x: x["moyenne"], reverse=True)[:1]
representants = meilleurs_hommes + meilleure_femme
groupe_valide = all(s["moyenne"] >= 10 for s in representants)
if not groupe_valide:
    print("Le groupe de représentation est annulé (moyenne non valide)")