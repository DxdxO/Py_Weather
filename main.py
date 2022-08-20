print ('Veuillez entrer la ville dont la météo est demandé') 
ville = input('Entrer la ville > ').lower()
Dico= {"abidjan":100, "daloa":45}

if ville in Dico.keys() :
    print("la temperature a {} est de : {} degre".format(ville, Dico[ville]))
else:
    print('ça ne marche pas')
        