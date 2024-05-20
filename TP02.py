'''
Travail Pratique 2
Jean-Hernan Bonilla et Maksen Chabi
e2171156 et e2362443
20-05-2024
'''
import csv
import json
import math


class DonneesGeo:
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = ville.strip() if isinstance(ville, str) else ville
        self.pays = pays.strip() if isinstance(pays, str) else pays
        self.latitude = float(latitude.strip()) if isinstance(latitude, str) else float(latitude)
        self.longitude = float(longitude.strip()) if isinstance(longitude, str) else float(longitude)

    def __str__(self):
        return f"{self.ville}, {self.pays}, {self.latitude}, {self.longitude}"


def lireDonneesCsv(nomFichier):
    listeObjDonneesGeo = []
    with open(nomFichier, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            try:
                ville, pays, latitude, longitude = row
                obj = DonneesGeo(ville, pays, latitude, longitude)
                listeObjDonneesGeo.append(obj)
            except ValueError as e:
                print(f"Erreur de conversion pour la ligne: {row}. Erreur: {e}")
    return listeObjDonneesGeo


def ecrireDonneesJson(nomFichier, listeObjDonneesGeo):
    listeDictDonneesGeo = [obj.__dict__ for obj in listeObjDonneesGeo]
    with open(nomFichier, 'w', encoding='utf-8') as file:
        json.dump(listeDictDonneesGeo, file, ensure_ascii=False, indent=4)


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(
        d_lon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    return R * c


def trouverDistanceMin(nomFichier):
    with open(nomFichier, 'r', encoding='utf-8') as file:
        listeObjDonneesGeo = json.load(file)
        listeObjDonneesGeo = [DonneesGeo(**geo) for geo in listeObjDonneesGeo]

    min_distance = float('inf')
    ville1 = ville2 = None

    for i in range(len(listeObjDonneesGeo)):
        for j in range(i + 1, len(listeObjDonneesGeo)):
            villeA = listeObjDonneesGeo[i]
            villeB = listeObjDonneesGeo[j]
            distance = haversine(villeA.latitude, villeA.longitude, villeB.latitude, villeB.longitude)
            if distance < min_distance:
                min_distance = distance
                ville1, ville2 = villeA, villeB

    with open('distances.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Ville 1', 'Ville 2', 'Distance'])
        writer.writerow([f'{ville1.ville}, {ville1.pays}', f'{ville2.ville}, {ville2.pays}', min_distance])

    print(
        f"Distance minimale en kilomètres entre 2 villes : Ville 1 : {ville1.ville} {ville1.pays} {ville1.latitude} {ville1.longitude} et Ville 2 : {ville2.ville} {ville2.pays} {ville2.latitude} {ville2.longitude} Distance en kilomètres : {min_distanc
