"""

Ce projet consiste a afficher la meteo d'une localité

"""

print ('Veuillez entrer la ville dont la météo est demandé') 
ville = input('Entrer la ville > ').lower() #je recupere la ville 

#ouverture du fichier villes.txt (f)
with open("villes.txt","r") as f :
    Dico = eval(f.read()) #eval renvoi le vrai type de la chaine de caratere retourné a="2"; b=eval(a)


if ville in Dico.keys() :
    print("la temperature a {} est de : {} degre".format(ville, Dico[ville]))
else:
    print('ça ne marche pas')
        