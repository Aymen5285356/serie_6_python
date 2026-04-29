personne = {
    "Nom": "Allali",
    "Prénom": "Soufiane",
    "Age": 19,
    "Téléphone": "06 11 22 33 44",
    "Email": "xyz@gmail.com"
}
personne["Email"] = "abc@gmail.com"
personne["Nom complet"] = personne["Nom"] + " " + personne["Prénom"]
personne["Ville"] = "Rabat"
del personne["Age"]
