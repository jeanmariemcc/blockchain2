import time
import sys
sys.path.append('backend')
from util.crypto_hash import crypto_hash


GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}

class Block:
    """
    Unit of storage for the Blockchain
      stores transactions and supports a cryptocurrency
    """
    def __init__ (self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce
        
    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce}'

            )
     
     
    @staticmethod   
    def mine_block(last_block, data):
         # mines a block based on given last_block and data
         #   until a block hash is found that meets the difficulty
         #   of the number of leading zeroes proof of work requirement
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = last_block.difficulty
        nonce = 0
        #hash = f'{timestamp}-{last_hash}' #temporary for testing
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
        
        while hash[0:difficulty] != '0' * difficulty:
            nonce +=1
            timestamp = time.time_ns()
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
            
        return Block(timestamp, last_hash, hash, data, difficulty, nonce)


    @staticmethod
    def genesis():
        # generate the first block
        return Block(**GENESIS_DATA)

        
def main():
    #block = Block('test_foo')
    #print(block)
    #print(f'block.py __name__: {__name__}')
    
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'firstblock - genesis')
    print(block)
    
if __name__ == '__main__':
    # only prints if called directly, not if called from blockchain.py
    main()
