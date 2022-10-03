import hashlib
import json

def crypto_hash(data):
    # returns sha-256 hash of given data
    stringifieddata = json.dumps(data)
    return hashlib.sha256(stringifieddata.encode('utf-8')).hexdigest()


def main():
    print(f"crypto_hash('foo'): {crypto_hash(2)}")
    
    
if __name__ == '__main__':
    # for testing
    main()