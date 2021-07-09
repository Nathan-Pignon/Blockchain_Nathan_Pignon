import uuid
import hashlib
import json
from os import listdir
from os.path import isfile, join
import os

class Bloc :

    def __init__(self, parent_hash=None, hash=None, base_hash=None):
        self.base_hash = base_hash
        self.hash = hash
        self.parent_hash = parent_hash
        self.weight = 0
        self.transactions = []        
    
    def check_hash(self, base_hash):
        hashed =  hashlib.sha256(base_hash.encode()).hexdigest()
        if hashed[:4] == "0000":
            self.hash = hashed
            return True
        else:
            return False
    
    
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
    
    
    def get_transaction(self):
        pass
    
    
    def info(self):
        print("Info du Bloc :")
        print("     Base hash : "+str(self.base_hash))
        print("     Hash : "+str(self.hash))
        print("     Parent hash : "+str(self.parent_hash))
        print("     Weight : "+str(self.weight))
        print("     Transactions : ")
        print(self.transactions)
    
    
    def get_weight(self):
        """ Chemin du .json qui aura comme nom son id """
        file = "content/blocs/"+str(self.hash)+".json"
        file_size = os.stat(file)
        self.weight = file_size.st_size
    
    
    def save(self):
        """ On rentre les données qui vont être présentes dans le .json """
        data = {
            "base_hash": self.base_hash,
            "hash": self.hash,
            "parent_hash": self.parent_hash,
            "weight": self.weight,
            "transactions": self.transactions
        }
        
        """ Chemin du .json qui aura comme nom son id """
        file = "content/blocs/"+str(self.hash)+".json"
        
        """ Ouverture (création s'il n'existe pas) du fichier avec les droits d'écritures pour sauvegarder les données """
        with open(file, "w") as filename:
            json.dump(data, filename)
            return self.hash
    
    
    def load(self, id_bloc=None):
        """ S'il ne met rien cela veut dire que l'on créé un nouveau bloc """
        if id_bloc != None:
            Verif = False
            """ On liste tous les blocs existants pour comparer les hash """
            files = [f for f in listdir("content/blocs/") if isfile(join("content/blocs/", f))]
            """ On supprime l'extension pour ne garder que le hash """
            files = ['.'.join(file.split('.')[:-1]) for file in files]
            """ On compare chaque hash existants avec celui saisie et si il existe on importe les données, sinon on redemande une saisie """
            for file in files:
                """ Si l'id saisie est identique à un id existant, on importe les données """
                if file == id_bloc:
            
                    """ Chemin du .json à ouvrir """
                    filename = "content/blocs/"+id_bloc+".json"
                    
                    """ Ouverture du .json avec droit de lecture """
                    with open(filename, "r") as data_json:
                        
                        """ Lecture des données """
                        data_load = json.load(data_json)
                        self.base_hash = data_load['base_hash']
                        self.hash = data_load['hash']
                        self.parent_hash = data_load['parent_hash']
                        self.weight = data_load['weight']
                        self.transactions = data_load['transactions']
                    Verif = True
            if Verif == False:
                return print("Le bloc saisi est inexistant")
            else:
                return True
        else:
            return False
    
