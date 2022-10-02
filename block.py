class Block:
    """
    Unit of storage for the Blockchain
      stores transactions and supports a cryptocurrency
    """
    def __init__ (self, data):
        self.data = data
        
    def __repr__(self):
        return f'Block - data: {self.data}'
        
def main():
    block = Block('test_foo')
    print(block)
    print(f'block.py __name__: {__name__}')
    
if __name__ == '__main__':
    # only prints if called directly, not if called from blockchain.py
    main()
