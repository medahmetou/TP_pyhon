
# Tp2 structures

# exo1

# jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
# ventes = [125000, 98000, 143500, 87000, 210000, 176500]

# # Afficher le total et la moyenne journalière des ventes. 
# total_ventes = sum(ventes)
# moyenne_ventes = total_ventes / len(ventes)

# print("Total des ventes de la semaine:", total_ventes)
# print("Moyenne des ventes de la semaine:", moyenne_ventes)

# # Afficher le nom du jour où les ventes ont été les plus fortes. 

# nom_jour_fort = jours[ventes.index(max(ventes))]
# print("Le jour de vente fort est:", nom_jour_fort )


# # Afficher les jours dont les ventes dépassent la moyenne. 

# for i in range(len(ventes)):  
#     if ventes[i] > moyenne_ventes:
#         print("Le jour de vente fort est  :", jours[i])


# # Afficher le classement des jours, de la meilleure à la plus faible vente.

# for i in range(len(ventes)):
#     for j in range(i + 1, len(ventes)):
#         if ventes[i] < ventes[j]:
#             ventes[i], ventes[j] = ventes[j], ventes[i]
#             jours[i], jours[j] = jours[j], jours[i]

# print("Classement des jours de la meilleure à la plus faible vente:")
# for i in range(len(ventes)):
#     print(f"{jours[i]}: {ventes[i]}")       

# print("4. Afficher le classement des jours, de la meilleure à la plus faible vente (méthode alternative).")
 
# couple =[]
# for i in range(len(ventes)):
#     couple.append((ventes[i], jours[i]))
# couple.sort(reverse=True)
# for i in range(len(couple)):
#     print(f"{couple[i][1]}: {couple[i][0]}")

# exxo2 

# l = [4, 7, 1, 9, 7, 3]

from django.conf.locale import pt


catalogue = {
    "P01": {"nom": "Ordinateur portable", "categorie": "Informatique","prix": 45000},
    "P02": {"nom": "Imprimante", "categorie": "Informatique","prix": 12000},
    "P03": {"nom": "Chaise de bureau", "categorie": "Mobilier","prix": 6500},
    "P04": {"nom": "Ramette papier", "categorie": "Fournitures","prix": 350},
}

catalogue["P05"] = {"nom": "Bureau", "categorie": "Mobilier","prix": 1800}

# Augmenter de 5 % (arrondi à l’unité) le prix des produits de la catégorie Informatique

for i in catalogue.values():
    if i["categorie"] == "Informatique":
        i["prix"] = round(i["prix"] * 1.05)
    print(f"{i['nom']}: {i['prix']}") 

