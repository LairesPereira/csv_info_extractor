import csv
from list_all_transactions import getTransactionsInfo
from crawlers import all_transactions_values, all_real_transaction_values, target_send_transactions,    target_recived_transactions

# writte all transactions in one file
all_transactions = getTransactionsInfo()
all_send_transactions_values = all_transactions_values(all_transactions, 'enviada')
all_recived_transactions_values = all_transactions_values(all_transactions, 'recebida')
all_real_transactions_send_values = all_real_transaction_values(all_transactions, 'enviada', 'laires')
all_real_transactions_recived_values = all_real_transaction_values(all_transactions, 'recebida', 'laires')

# print(all_real_transactions_send_values)

def all_transactions_to_writte():
    with open('list_of_all_transactions.csv', mode='w', newline='') as csvfile:
        writter = csv.DictWriter(csvfile, delimiter=',', fieldnames=all_transactions[0].keys())
        writter.writeheader()
        writter.writerows(all_transactions)
        
def all_recived_values_to_writte():
    with open('all_recived_values.csv', mode='w', newline='') as csvfile:
        writter = csv.DictWriter(csvfile, delimiter=',', fieldnames=all_real_transactions_recived_values.keys())
        writter.writeheader()
        writter.writerow(all_real_transactions_recived_values)

def all_send_values_to_write():
    with open('all_send_values_to_write.csv', mode='w', newline='') as csvfile:
        writter = csv.DictWriter(csvfile, delimiter=',', fieldnames=all_real_transactions_send_values.keys())
        writter.writeheader()
        writter.writerow(all_real_transactions_send_values)

def all_specific_send_transactions_to_write():
    complete_values_list = []
    checked_names = []
    for transaction in all_transactions:
        if not transaction['name'] in checked_names:
            if 'enviada' in transaction['type']:
                complete_values_list.append(target_send_transactions(all_transactions, transaction['name']))
                checked_names.append(transaction['name'])

    with open('all_specific_send_transactions.csv', mode='w', newline='') as csvfile:
        writter = csv.DictWriter(csvfile, delimiter=',', fieldnames=complete_values_list[-1].keys())
        writter.writeheader()
        writter.writerows(complete_values_list)

def all_specific_recived_transactions_to_write():
    complete_values_list = []
    checked_names = []
    for transaction in all_transactions:
        if not transaction['name'] in checked_names:
            if 'recebida' in transaction['type']:
                complete_values_list.append(target_recived_transactions(all_transactions, transaction['name']))
                checked_names.append(transaction['name'])

    with open('all_specific_recived_transactions.csv', mode='w', newline='') as csvfile:
        writter = csv.DictWriter(csvfile, delimiter=',', fieldnames=complete_values_list[-1].keys())
        writter.writeheader()
        writter.writerows(complete_values_list)
        
# all_specific_send_transactions_to_write()
all_specific_recived_transactions_to_write()
# all_transactions_to_writte()
# all_recived_values_to_writte()
# all_send_values_to_write()