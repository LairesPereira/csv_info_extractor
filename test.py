from list_all_transactions import getTransactionsInfo
import numpy as np
import pandas as pd

transactions = getTransactionsInfo('10_nubank_outubro_2023.csv')
# print(transactions[0])

index = 0
for transaction in transactions:
    transactions_data_frame = pd.DataFrame(transaction, index=[index])
    index += 1
    print(transactions_data_frame)