import csv
from list_all_transactions import getTransactionsInfo
from crawlers import all_transactions_values, all_real_transaction_values, target_send_transactions, target_recived_transactions
import shutil
from matplotlib import *

import os
all_files = os.listdir('./csv_files')
if '.DS_Store' in all_files:
    all_files.remove('.DS_Store')
all_files.sort()

def create_folders_structures(): 
    all_files = os.listdir('./csv_files')
    if '.DS_Store' in all_files:
        all_files.remove('.DS_Store')
    all_files.sort()

    for file in all_files:
        directory = file.split('.csv')[0]
        parent_dir = "./month_sheets/"
        path = os.path.join(parent_dir, directory) 
        if not os.path.exists(path):
            os.mkdir(path) 
            print("Directory '%s' created" %directory) 


def all_transactions_to_writte(file_name):
    with open(file_name, mode='w', newline='') as csvfile:
        writter = csv.DictWriter(csvfile, delimiter=',', fieldnames=all_transactions[0].keys())
        writter.writeheader()
        writter.writerows(all_transactions)
        shutil.copy('./' + file_name, './month_sheets/' + file_name.split('.csv')[0]) 
        os.remove(file_name)
        
        
        
def all_recived_values_to_writte(file_name, all_real_transactions_recived_values):
    with open(file_name, mode='w', newline='') as csvfile:
        src = './' + file_name
        dest = './month_sheets/' + file_name.split('.csv')[0]
        base, extension = os.path.splitext(file_name)
        new_name = f'all_recived_values_{base}{extension}'
        complete_path_destination = os.path.join(dest, new_name)

        writter = csv.DictWriter(csvfile, delimiter=',', fieldnames=all_real_transactions_recived_values.keys())
        writter.writeheader()
        writter.writerow(all_real_transactions_recived_values)
        shutil.move(src, complete_path_destination)
    

def all_send_values_to_write(file_name, all_send_values_to_write):
    with open(file_name, mode='w', newline='') as csvfile:
        src = './' + file_name
        dest = './month_sheets/' + file_name.split('.csv')[0]
        base, extension = os.path.splitext(file_name)
        new_name = f'all_send_values_{base}{extension}'
        complete_path_destination = os.path.join(dest, new_name)

        writter = csv.DictWriter(csvfile, delimiter=',', fieldnames=all_send_values_to_write.keys())
        writter.writeheader()
        writter.writerow(all_real_transactions_send_values)
        shutil.move(src, complete_path_destination)


def all_specific_send_transactions_to_write(file_name, all_transactions):
    src = './' + file_name
    dest = './month_sheets/' + file_name.split('.csv')[0]
    base, extension = os.path.splitext(file_name)
    new_name = f'all__specific_send_values_{base}{extension}'
    complete_path_destination = os.path.join(dest, new_name)

    complete_values_list = []
    checked_names = []
    for transaction in all_transactions:
        if not transaction['name'] in checked_names:
            if 'enviada' in transaction['type']:
                complete_values_list.append(target_send_transactions(all_transactions, transaction['name']))
                checked_names.append(transaction['name'])

    with open(file_name, mode='w', newline='') as csvfile:
        writter = csv.DictWriter(csvfile, delimiter=',', fieldnames=complete_values_list[-1].keys())
        writter.writeheader()
        writter.writerows(complete_values_list)
        shutil.move(src, complete_path_destination)


def all_specific_recived_transactions_to_write(file_name, all_transactions):
    src = './' + file_name
    dest = './month_sheets/' + file_name.split('.csv')[0]
    base, extension = os.path.splitext(file_name)
    new_name = f'all__specific_recived_values_{base}{extension}'
    complete_path_destination = os.path.join(dest, new_name)
    
    complete_values_list = []
    checked_names = []
    
    for transaction in all_transactions:
        if not transaction['name'] in checked_names:
            if 'recebida' in transaction['type']:
                complete_values_list.append(target_recived_transactions(all_transactions, transaction['name']))
                checked_names.append(transaction['name'])

    with open(file_name, mode='w', newline='') as csvfile:
        writter = csv.DictWriter(csvfile, delimiter=',', fieldnames=complete_values_list[-1].keys())
        writter.writeheader()
        writter.writerows(complete_values_list)
        shutil.move(src, complete_path_destination)


create_folders_structures()

for file in all_files:
    all_transactions = getTransactionsInfo(file)
    all_send_transactions_values = all_transactions_values(all_transactions, 'enviada')
    all_recived_transactions_values = all_transactions_values(all_transactions, 'recebida')
    all_real_transactions_send_values = all_real_transaction_values(all_transactions, 'enviada', 'laires')
    all_real_transactions_recived_values = all_real_transaction_values(all_transactions, 'recebida', 'laires')
    all_specific_send_transactions_to_write(file ,all_transactions)
    all_specific_recived_transactions_to_write(file, all_transactions)
    all_transactions_to_writte(file)
    all_recived_values_to_writte(file, all_real_transactions_recived_values)
    all_send_values_to_write(file, all_real_transactions_send_values)