#compute the hash of any given output
import hashlib

#print(hashlib.sha256("{name}".encode()).hexdigest())

NONCE_limit = 10000000000000000000000

zero = 19

def mining(block_number,transactions, previous_hash):
    for nonce in range(NONCE_limit):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_find = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_find.startswith("0" * zero):
            print(f"Found Hash with Nonce:  {nonce}")
            return hash_find

    return -1

block_number = 55
transactions = "3289at231876"
previous_hash = "5487354uv189"

mining(block_number, transactions, previous_hash)

combo_text = str(block_number) + transactions + previous_hash +str(1156682)
print(hashlib.sha256(combo_text.encode()).hexdigest())
