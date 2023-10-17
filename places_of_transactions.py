from list_all_transactions import getTransactionsInfo
from crawlers import target_transactions


# pega o nome de cada pessoa no extrato
# e retorna o valor total das transações naquele nome especifico
def list_target_transactions():
    all_transactions = getTransactionsInfo()
    list_of_names = []
    final_list_target_transactions = []

    for transaction in all_transactions:
        if(transaction['name'].lower() not in list_of_names):
            list_of_names.append(transaction['name'].lower())

    for name in list_of_names:
        operations = target_transactions(all_transactions, 'enviada', name)
        if(operations['sum_of_target_operation'] > 0):
            final_list_target_transactions.append(operations)
        elif(operations['sum_of_target_operation'] < 0):
            final_list_target_transactions.append(operations)
    
    return final_list_target_transactions
    
