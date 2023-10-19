from list_all_transactions import getTransactionsInfo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from crawlers import target_recived_transactions
from list_all_transactions import getTransactionsInfo

# raw_data_path = '10_nubank_outubro_2023.csv'
# raw_data = getTransactionsInfo(raw_data_path)
# print(raw_data)


# plt.style.available

# plt.style.use()

plt.rcParams['figure.figsize'] = (20, 7)
raw_data = pd.read_csv('month_sheets/10_nubank_outubro_2023/all__specific_send_values_10_nubank_outubro_2023.csv')
print(raw_data)
plt.plot([raw_data.sum_of_target_operation])
# plt.ylabel('Valores em R$')
# plt.xlabel('Tempo')
plt.show()



# def target_send_transactions(list_of_transactions, owner):
#     sum_value = 0
#     number = 0
#     name = ''

#     for transaction in list_of_transactions:
#         if 'enviada' in transaction['type']:
#             if owner in transaction['name']:
#                 if float(transaction['value']) < 0:
#                     sum_value += float(transaction['value'])
#                     number += 1
#                     name = transaction['name']
    
#         target_transactions_info = {
#             'name': name,
#             'number_of_operations': number,
#             'sum_of_target_operation': sum_value
#         }
    
#     return target_transactions_info
