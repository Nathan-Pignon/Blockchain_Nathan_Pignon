import hashlib
import json
import string
import random

class Chain :

    def __init__(self):
        self.blocks = []
        self.last_transaction_number = 0
        self.generate_hash()
        
        
    def generate_hash(self):
        hash = ""
        while not self.verify_hash(hash):
            random_str = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            hash = hashlib.sha256(random_str.encode()).hexdigest()
        print(random_str)       
        
        
    def verify_hash(self, hash):
        if hash[:4] == "0000":
            return True
        else:
            return False
            
        
    def add_block(self, block):
        self.blocks.append(block)
            
        
    def get_block(self):
        pass
            
        
    def add_transaction(self):
        pass
    

MyChain = Chain()
        