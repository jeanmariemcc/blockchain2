import sys
sys.path.append('backend.blackchain')
from block import Block


class Blockchain:
    """
    Blockhain - implemented as a list of blocks,
        each block contains sets of transactions
    """
    def __init__(self):
        self.chain = [Block.genesis()]
        
    def add_block(self, data):
        #last_block = self.chain[-1] 
        #self.chain.append(Block(data))
        self.chain.append(Block.mine_block(self.chain[-1], data)) # changed after added mine_block to Block
        
    def __repr__(self):
        return f'Blockchain: {self.chain}'
    
    
    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incomiing chain.
        Enforce:
         - the chain must start with a genesis block
         - blocks must be formatted correctly
        """
        if chain[0] != Block.genisis():
            raise Exception('The genesis block is not valid')
        
        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)
 
    
def main(): 
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    print(blockchain.__dict__)
      
      
if __name__ == '__main__':
    main()