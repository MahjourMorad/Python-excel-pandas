# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:25:09 2021

@author: MAHJOUR
"""

import pandas as pd
import numpy as np
import random
# Create a Pandas dataframe from the data.
# df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
#df = pd.DataFrame({'Data': np.arange(100),'Prix': np.random.sample(100) * 684})

print(np.random.choice(range(20), 10, replace=False))



couleurs = ['jaune','rouge','vert','bleu','violet','noir','blanc','rose','orange','gris','bleu nuit','framboise','fraise','cobalt','citron']
produit = ['Ajrak','Áo dài','Bikini ','Body ','Burkini','Burqa','Bustier','Bustier tubulaire','Cache-cœur','Camisole ','Capri ','Casaquin','Chainse','Châle','Chemisier','China poblana','Cobijada','Combishort','Corps à baleines','Corsage','Corselet','Corset','Crinoline','Cycliste ','Djebba constantinoise','Dos nu','Fascia pectoralis','Frumka','Furisode','Gharara','Gomesi','Guimpe','Haïk (vêtement)','Hassara','Haut court','Hidjab','Hot pants','Houli','Huipil','Jupe crayon','Jupon','Juste ','Kaba Ngondo','Kokochnik','Le smoking','Legging','Lehenga','Letnik','Mlaya','Maillot de bain une pièce','Mantille','Microkini','Minijupe','Mola ','Monokini']
saison = ['Q1','Q2','Q3','Q4']
Fabrication = ['france','chine ','chine ','chine','chine','chine','tunisie']
Group = ['GRP1','GRP2','GRP3','GRP4','GRP5','GRP6','GRP7','GRP8']
listProduit =[]
listSaison = []
listCouleurs = []
listSexe = []
listOFGroup = []
listOFabrication = []
listofmatiere = []
listofPrices = []
listQuantite = []
listCodemag = []

# Remplissage des listes des prouits 
for name in range(10000):
    listProduit.append(random.choice(produit))
    
    
#remplissage des listes des saison
for name in range(10000):
    listSaison.append(random.choice(saison))
    
    
#remplissage des listes des couleurs
for name in range(10000):
    listCouleurs.append(random.choice(couleurs))
    
#remplissage des listes des sexes
for name in range(10000):
    listOFabrication.append(random.choice(Fabrication))
    
    
#remplissage des listes des groupes
for name in range(10000):
    listOFGroup.append(random.choice(Group))
    
#remplissage des listes des quantite
for name in range(10000):
    listQuantite.append(random.randint(0, 780))
    
#remplissage des listes des matieres premieres
for name in range(10000):
    listCodemag.append(random.randint(230, 330))
    
    
    
#remplissage des listes des matieres premieres
#for name in range(100):
#    listofPrices.append(random.choice(matierePremiere))
    
# initialisation des listes des noms, prenom,civilit , villes .....
# code_produit
#code_couleur
#libelle_long
# type_produit
#code_group

#code_sous_rayon
#origine_fabrication
#matiere principale
# pri_de_ventes    
    
df = pd.DataFrame({'code_produit': np.arange(98420,108420),
                   'CodeMag':listCodemag,
                   'Quanrite_vendu':listQuantite,
                   'Montant':listSaison,
                   'Code_client':listOFGroup,
                   'Code_vendeur':listOFabrication,
                   'Code_saison': listSaison
                  # 'sexe':listSexe,
                   #'Ville':listVille
                   }
                  )

#'num_carte': np.random.sample(100) * 684

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('Ventes.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()