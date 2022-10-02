class Block:
    """
    Unit of storage for the Blockchain
      stores transactions and supports a cryptocurrency
    """
    def __init__ (self, data):
        self.data = data
        
    def __repr__(self):
        return f'Block - data: {self.data}'
        

class Blockchain:
    """
    Blockhain - implemented as a list of blocks,
        each blcok contains sets of transactions
    """
    def __init__(self):
        self.chain = []
        
    def add_block(self, data):
        self.chain.append(Block(data))
        
    def __repr__(self):
        return f'Blockchain: {self.chain}'
        
        
blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')

print(blockchain.__dict__)
        