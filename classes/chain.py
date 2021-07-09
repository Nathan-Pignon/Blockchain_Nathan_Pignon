import hashlib
import json
import random
import string

from classes.bloc import Bloc


class Chain :

    def __init__(self):
        self.blocks = []
        self.base_hash = 0
        self.last_transaction_number = 0
        
        
    def generate_hash(self):
        hash = ""
        while not self.verify_hash(hash):
            random_str = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            hash = hashlib.sha256(random_str.encode()).hexdigest()
        print(random_str)
        return random_str       
        
        
    def verify_hash(self, hash):
        if hash[:4] == "0000":
            return True
        else:
            return False
            
        
    def add_block(self):
        hash_found = self.generate_hash()
        new_block = Bloc(self.blocks[len(self.blocks) - 1].hash,
                          hash_found, self.base_hash)
        if new_block.check_hash(hash_found):
            print("Le hash est validé")
            self.blocks.append(new_block)
            new_block.save()
            new_block.get_weight()
            new_block.save()
            
        
    def get_block(self, hash):
        get_bloc = Bloc()
        get_bloc.load(hash)
        self.blocks.append(get_bloc)
            
        
    def add_transaction(self):
        pass
    

MyChain = Chain()
        