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
            f'timestamp: {self.timestamp},'
            f'last_hash: {self.last_hash},'
            f'hash: {self.hash}'
            f'data: {self.data}'
            )
        
def main():
    block = Block('test_foo')
    print(block)
    print(f'block.py __name__: {__name__}')
    
if __name__ == '__main__':
    # only prints if called directly, not if called from blockchain.py
    main()
