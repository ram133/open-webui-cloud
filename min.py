# https://github.com/ram133/open-webui-cloud
import json
import hashlib
import os

LEDGER = "min.json"

def init_chain():
    if os.path.exists(LEDGER):
        with open(LEDGER, 'r') as f:
            return json.load(f)
    genesis = {
        "supply": 1000000,
        "balances": {"treasury": 1000000},
        "history": [{"from": "genesis", "to": "treasury", "amount": 1000000, "hash": "0"}]
    }
    save_chain(genesis)
    return genesis

def save_chain(data):
    with open(LEDGER, 'w') as f:
        json.dump(data, f, indent=2)

def transfer(sender, recipient, amount):
    chain = init_chain()
    if chain["balances"].get(sender, 0) < amount:
        return False, "Insufficient balance"
    
    chain["balances"][sender] -= amount
    chain["balances"][recipient] = chain["balances"].get(recipient, 0) + amount
    
    prev_hash = chain["history"][-1]["hash"]
    block_data = f"{sender}{recipient}{amount}{prev_hash}"
    block_hash = hashlib.sha256(block_data.encode()).hexdigest()
    
    chain["history"].append({"from": sender, "to": recipient, "amount": amount, "hash": block_hash})
    save_chain(chain)
    return True, block_hash

if __name__ == "__main__":
    chain = init_chain()
    print(f"MinCoin Ledger Active. Treasury Balance: {chain['balances'].get('treasury', 0)}")
