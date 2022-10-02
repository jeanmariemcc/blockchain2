class Block:
    """
    Unit of storage for the Blockchain
      stores transactions and supports a cryptocurrency
    """
    def __init__ (self, data):
        self.data = data
        

class Blockchain:
    """
    Blockhain - implemented as a list of blocks,
        each blcok contains sets of transactions
    """
    def __init__(self):
        self.chain = []
        
    def add_block(self, data):
        self.chain.append(Block(data))
        