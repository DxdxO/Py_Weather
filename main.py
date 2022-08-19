"""

Ce projet consiste a afficher la meteo d'une localité

"""

print ('Veuillez entrer la ville dont la météo est demandé') 
ville = input('Entrer la ville > ').lower() #je recupere la ville 

with open("villes.txt","r") as f :
    Dico = eval(f.read())


if ville in Dico.keys() :
    print("la temperature a {} est de : {} degre".format(ville, Dico[ville]))
else:
    print('ça ne marche pas')
        