class Block:
    """
    Unit of storage for the Blockchain
      stores transactions and supports a cryptocurrency
    """
    def __init__ (self, data):
        self.data = data
        
    def __repr__(self):
        return f'Block - data: {self.data}'
        
