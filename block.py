import time

def mine_block(last_block, data):
    # mines a block based on given last_block and data
    timestamp = time.time_ns()
    last_hash = last_block.hash
    hash = f'{timestamp}-{last_hash}' #temporary for testing
    
    return Block(timestamp, last_hash, hash, data)


def genesis():
    # generate the first block
    return Block(1, 'genesis_last_hash', 'genesis_hash', [])


class Block:
    """
    Unit of storage for the Blockchain
      stores transactions and supports a cryptocurrency
    """
    def __init__ (self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        
    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}'
            )
        
def main():
    #block = Block('test_foo')
    #print(block)
    #print(f'block.py __name__: {__name__}')
    
    genesis_block = genesis()
    block = mine_block(genesis_block, 'firstblock - genesis')
    print(block)
    
if __name__ == '__main__':
    # only prints if called directly, not if called from blockchain.py
    main()
