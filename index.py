from list_all_transactions import getTransactionsInfo

all_transactions = getTransactionsInfo()

# o parametro tipo de operações
# devem ser sempre 'enviada' ou 'recebida'
def all_transactions_values(list_of_transactions, type_of_operation):
    total_sum = 0
    for transaction in list_of_transactions:
        if(f'{type_of_operation}' in transaction['type'].lower()):
            total_sum += float(transaction['value'])
    
    return total_sum


# algumas transacoes podem vir do proprio dono da conta
# atraves de outras contas em seu nome, devemos ignorar
# essas transações para termos o real montante de valor
# recebido ou enviado. O parametro owner deve ter o nome registrado que 
# está fazendo transacoes cruzadas
def all_real_transaction_values(list_of_transactions, type_of_operation, owner):
    total_sum = 0
    crossed_transactions = 0
    crossed_transactions_value = 0
    
    for transaction in list_of_transactions:
        if('laires duarte soares' in transaction['name'].lower()): continue

        if(not f'{owner}' in transaction['name'].lower()):    
            if(f'{type_of_operation}' in transaction['type'].lower()):
                total_sum += float(transaction['value'])
       
        elif((f'{owner}' in transaction['name'].lower()) and f'{type_of_operation}' in transaction['type'].lower()):        
            crossed_transactions_value += float(transaction['value'])
            crossed_transactions += 1
    
    return  {
            'total_sum:': total_sum,
            'crossed_transactions:': crossed_transactions,
            'crossed_transactions_value: ': crossed_transactions_value,
            }

full_result = all_transactions_values(all_transactions, 'recebida')
real_result_value = all_real_transaction_values(all_transactions, 'enviada', 'laires')
real_result_recived = all_real_transaction_values(all_transactions, 'recebida', 'laires')
# print(real_result_value)
# print(real_result_recived)



def target_transactions(list_of_transactions, type_of_operation, owner):

    number_of_operations = 0
    sum_of_target_operations = 0
    for transaction in list_of_transactions:
        if(type_of_operation in transaction['type'].lower()):
            if(owner in transaction['name'].lower()):
                sum_of_target_operations += float(transaction['value'])
                number_of_operations += 1
                # print(transaction['name'], transaction['value'])

    # print(f'{number_of_operations} operações em {owner} somando:', sum_of_target_operations)
    return sum_of_target_operations





