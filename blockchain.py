from block import Block

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
    
def main(): 
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    print(blockchain.__dict__)
      
      
if __name__ == '__main__':
    main()