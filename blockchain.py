blockchain = []

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transactions(transaction_ammount, last_transaction = [1]):
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_ammount])

def get_transaction_value():
    user_input = float(input('Your transaction amount please... '))
    return user_input

def get_user_choice():
    user_choice = input()
    return user_choice

def print_blockchain_elements():
    for block in blockchain:
        print("Output a block")
        print(block)


while True:
    print("\nPlease, choose:")
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transactions(tx_amount, get_last_blockchain_value())
        print("Transaction added successfully!")
        print("\n")
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break    
    else:
        print("\n!!!Please, choose correct number!!!")
        continue
    
print("Done!")