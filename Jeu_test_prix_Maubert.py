#!/usr/bin/env python
# coding: utf-8

# # GÉNÉRER DES NOMS DE BOISSON ALEATOIREMENT, ÉVALUER LA CONNAISSANCE DU PRIX ET VÉRIFIER L'EXACTITUDE DES RÉPONSES

# In[264]:


import sys
import pymsgbox
import random


# In[ ]:


Prix = {"expresso": 2.3, 
         "noisette" : 2.5,
         "doublecafe" : 4.2,'cafeamericain' : 4.2, "cafecreme": 4.2, 
         "chocolatchaud": 4.5,
         "cappucino": 5, "macchiato" : 5, 
         "cafechocviennois" : 5.5,
         "citronchaudbio": 5,
         "tea": 4.2,
         "infusion": 4.2,
         "vinchaud": 5,
         "grog": 6.5,
         "irishcoffee": 8.5,
         "orangecitronbiopresses" : 5.5,
         "coca": 4.8, "orangina": 4.8, "diabolo": 4.8, "sweppes": 4.8, "limonade": 4.8, "icetea": 4.8, "jusdefruits": 4.8,
         "1664_50CL en HH": 6, "grim_50CL en HH": 6, "brooklyn_50CL en HH": 6, "colomba_50CL en HH": 6 , "piconbiere_50CL en HH": 6 ,
"1664_50CL hors HH": 8.5, "grim_50CL hors HH": 9, "brooklyn_50CL hors HH": 9, "colomba_50CL hors HH": 9 , "piconbiere_50CL hors HH": 10 ,
         "1664_25CL": 4.6, "grim_25CL": 4.8, "brooklyn_25CL": 4.8, "colomba_25CL": 4.8, "piconbiere_25CL" : 5,
         "galliaIPA" : 6, "tripel": 6, "corona": 6,
         "kir": 5, "ricard": 5, "suze": 5, "porto": 5, "martini": 5, "campari": 5, 
         "americanomaison": 6,
         "coteprovence_selonles3vol" : "5-15.5-24", "chenin_selonles3vol": "4.5-14.5-22", "chardonnay_selonles3vol": "5-15.5-24", "viognier_selonles3vol": "5-15.5-24", "pinot_selonles3vol": "4.5-14.5-22", "verdot_selonles3vol": "5-15.5-24", "cotedurhone_selonles3vol": "5-15.5-24","bordeaux_selonles3vol": "5-15.5-24",
         "coupechamp": "6.5 en HH - 8.5 hors HH",
         "kir": 9.5,
         'btlechamp: 50'
         "vodka" : 7, "vodka + jus orange" : 9,
         "beefeater" : 7, "hendricks" : 10, 
         "tipunch" : 7,"havana": 7, "clément": 8, "yellow" : 8, "troisrivieres" : 10,"diplomatico" : 10,"bally": 12,
         "ballantines": 7, "jack": 8, "aberlour": 8, "oban": 10, "nikka": 10, "lagavulin": 12,
         "get27": 7, "poire" : 10 , "calvados": 10, "chartreuse": 10, "armagnac": 10, "cognac": 10,
         "negroni en HH" : 6, "spritz en HH": 6, "moscowmule": 6, "mojito en HH": 6, "caïpi en HH":6,"virginmojito en HH": 6,
         "negroni hors HH": 9, "spritz hors HH": 9, "moscowmule hors HH": 9, "mojito hors HH": 9, "caïpi hors HH": 9,"virginmojito hors HH" :7}


# In[273]:


def generation_nom_boisson(Prix):
    #génération d'un prix aléatoire
    boisson=random.choice(list(Prix.keys()))
    return boisson

def test(Prix):
    
    #génération d'un prix aléatoire
    boisson= generation_nom_boisson(Prix)
    #Msg Box popup pour poser la question sur cettte boisson
    proposition_de_demarage_du_jeu = pymsgbox.alert('Quel est le prix de:' +" " + boisson, 'La devinette', "Allez je me le tente!")
    
    response = pymsgbox.prompt('Vas-y propose ton prix !!?')
    #si la réponse est la bonne
    if response == str(Prix[boisson]):
        resultat = pymsgbox.confirm('Bien ouej! Tu veux rejouer tout de suite ou reprendre plus tard?', 'Fin du game?', ["Je rejoue!", 'La flemme!'])
    
    #si le user veut rejouer --> boucle sur la génération aléatoire d'un nom de boisson
        if resultat == "Je rejoue!":
            test(Prix)
        elif resultat == "La flemme!":
            pymsgbox.alert('A plus tard !', 'Fin du Game !!!', "A + !")
    #sinon, si la réponse est fausse
    elif response == None:
        pymsgbox.alert('A plus tard !', 'Fin du Game !!!', "A + !")
    else:
        resultat = pymsgbox.confirm('Et non t es pas encore au point sur ta carte, Tu veux une deuxième chance ou tu veux la réponse desuite?', 'Fin du game?', ["Deuxième chance!", 'La flemme balance la réponse!'])
        #si il y a 2e essaie alors le résultat de pymsgbox.confirm nous permet de boucler sur response
        if resultat == "Deuxième chance!":
            #boucle sur response
            response = pymsgbox.prompt('Attention, deuxième chance pour le prix de/du ' +" " + boisson, 'La devinette')
            if response == str(Prix[boisson]):
                resultat = pymsgbox.confirm('Top! 2e round concluant!', 'Fin du game?', ["Je rejoue!", 'La flemme!'])
                #si le user veut rejouer --> boucle sur la génération aléatoire d'un nom de boisson
                if resultat == "Je rejoue!":
                    test(Prix)
                elif resultat == "La flemme!":
                    pymsgbox.alert('A plus tard !', 'Fin du Game !!!', "A + !" )
            elif response == None:
                pymsgbox.alert('A plus tard !', 'Fin du Game !!!', "A + !")
            else:
                pymsgbox.alert("La réponse est .... :" + "\n" + str(Prix[boisson]) + " ma gueule :) ! ", 'Fin du Game !!!', "OK maintenant c dans ma ptite tête !!" )
        else:
                pymsgbox.alert("La réponse est .... :" + "\n" + str(Prix[boisson]) + " ma gueule :) ! ", 'Fin du Game !!!', "OK maintenant c dans ma ptite tête !!" )

test(Prix)


# In[274]:


def usage(error_message=False):
    """
    Instructions pour utiliser ce script Jeu_test_prix_Maubert.py.    
    """
    print("Ligne de commande à écrire: python3 PATH/TO/Jeu_test_prix_Maubert.py [OPTIONS...]")
    print ("Utiliser l'option -h, -? ou --help pour afficher ce message dans le termainal\n")

    if error_message:
        print ("UsageError:", error_message)
        sys.exit(500)
    else:
        sys.exit(0)

def main():
    option_dict = {}
    for arg in sys.argv:
        if arg == "Jeu_test_prix_Maubert.py":
            usage()
        if arg in ["-h","-?","--help"]:
            usage()
        elif arg in ["-v","--verbose","-e","--error"]:
            option_dict[arg] = True
        else:
            usage('Argument "%s" not recognized'%arg)
        if len(sys.argv) == 1:
            usage()
    try:
        test(Prix)
    except:
        if "-e" in option_dict.keys() or "--error" in option_dict.keys():
            raise
        else:
            usage('An option is missing, incorrect or not authorized')

if __name__ == '__main__':
    main()


# In[ ]:




