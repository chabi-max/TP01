
def afficher_menu():
    print("1- Lire les données du fichier csv, créer les objets et afficher les données.")
    print("2- Sauvegarder les données dans un fichier .json.")
    print(
        "3- Lire les données du fichier .json, déterminer et afficher les données associées à la distance minimale entre deux villes et sauvegarder les calculs dans distances.csv.")
    print("Entrez un numéro pour choisir une option ou appuyez sur 'q' pour quitter :")


def main():
    listeObjDonneesGeo = []
    while True:
        afficher_menu()
        choix = input()
        if choix == '1':
            listeObjDonneesGeo = lireDonneesCsv('Donnees.csv')
            for obj in listeObjDonneesGeo:
                print(obj)
            input("Appuyez sur une touche pour continuer...")
        elif choix == '2':
            if listeObjDonneesGeo:
                ecrireDonneesJson('Donnees.json', listeObjDonneesGeo)
            else:
                print("Veuillez d'abord lire les données du fichier CSV (Option 1).")
        elif choix == '3':
            if listeObjDonneesGeo:
                trouverDistanceMin('Donnees.json')
            else:
                print("Veuillez d'abord sauvegarder les données dans un fichier JSON (Option 2).")
        elif choix == 'q':
            break
        else:
            print("Choix non valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()