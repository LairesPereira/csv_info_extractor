from list_all_transactions import getTransactionsInfo
from index import target_transactions

# pega o nome de cada pessoa no extrato
# e retorna o valor total das transações naquele nome especifico

all_transactions = getTransactionsInfo()
list_of_names = []

for transaction in all_transactions:
    if(transaction['name'].lower() not in list_of_names):
        list_of_names.append(transaction['name'].lower())

print(list_of_names)

for name in list_of_names:
    operation_to = target_transactions(all_transactions, 'recebida', name)
    if(operation_to > 0):
        print(f'{name}: ', operation_to)
    
