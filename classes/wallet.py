import uuid
import json
from os import listdir
from os.path import isfile, join


class Wallet :

    """ Initialisation de la class """
    def __init__(self):
        load = self.load()
        if load == False:
            self.balance = 0
            self.history = []
            self.unique_id = self.generate_unique_id()
            self.save()
        
    def generate_unique_id(self):
        
        Verif = False
        
        """ Tant que notre id n'est pas unique, on regénère un id et on refait les vérifications """
        while Verif == False:
            
            """ Génération d'un id """
            unique_id = uuid.uuid4().int
            
            """ On passe le booléen de vérif à True pour sortir de la boucle s'il n'y a pas d'erreurs """
            Verif = True
            
            """ On liste tous les wallets existants pour comparer les id """
            files = [f for f in listdir("content/wallets/") if isfile(join("content/wallets/", f))]
            
            """ On supprime l'extension pour ne garder que l'id """
            files = ['.'.join(file.split('.')[:-1]) for file in files]
            
            """ On compare chaque unique_id existants avec le nouveau et si il existe on renvoie False et on en regénère un nouveau """
            for file in files:
                
                """ Si le nouvel id est identique à un id existant, on passe le booléen de verif à False pour relancer la boucle """
                if file == str(unique_id):
                    Verif = False
        
        return unique_id
    
    def add_balance(self, int):
        self.balance += int

    def sub_balance(self, int):
        self.balance -= int
    
    def send():
        pass
    
    def save(self):
        """ On rentre les données qui vont être ^résentes dans le .json """
        data = {
            "unique_id": self.unique_id,
            "balance": self.balance,
            "history": self.history
        }
        
        """ Chemin du .json qui aura comme nom son id """
        file = "content/wallets/"+str(self.unique_id)+".json"
        
        """ Ouverture (création s'il n'existe pas) du fichier avec les droits d'écritures pour sauvegarder les données """
        with open(file, "w") as filename:
            json.dump(data, filename)
            
    def load(self):
        """ On demande si l'utilisateur veut récupérer un wallet existant """
        id_wallet = input("Quel est l'id de votre wallet ?")
        
        """ S'il ne met rien cela veut dire que l'on créé un nouveau wallet """
        if id_wallet != "" and id_wallet != " ":
            
            """ Chemin du .json à ouvrir """
            file = "content/wallets/"+id_wallet+".json"
            
            """ Ouverture du .json avec droit de lecture """
            with open(file, "r") as data_json:
                
                """ Lecture des données """
                data_load = json.load(data_json)
                self.unique_id = data_load['unique_id']
                self.balance = data_load['balance']
                self.history = data_load['history']
            return True
        else:
            return False
        
            
MyWallet = Wallet()
