blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_ammount, last_transaction = [1]):
    blockchain.append([last_transaction, transaction_ammount])

def get_user_input():
    user_input = float(input('Your transaction amount please... '))
    return user_input

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)