
from os import listdir
from os.path import isfile, join
from classes.bloc import Bloc
from classes.chain import Chain
from classes.wallet import Wallet

def my_wallet():
    w = Wallet()
    Ajout_balance = input("Combien voulez-vous dans votre porte-monnaies ?")
    w.add_balance(int(Ajout_balance))
    w.save()
    id_wallet = input("Entrez le numéro d'un Wallet si vous voulez en charger un ")
    w.load(id_wallet)


def my_chain():
    print("Chargement du bloc de base...")
    c = Chain()
    b = Bloc()
    b.load("00")
    c.get_block("00")
    print("Création d'un nouveau Bloc...")
    new_bloc = c.add_block()
    b.load(new_bloc)
    b.info()
    load_hash = input("Entrez le hash d'un bloc pour entrer dedans (Faites 'Entrer' pour rester dans le même) : ")
    b.load(load_hash)
    b.info()

if __name__ == '__main__':
    my_wallet()
    my_chain()
