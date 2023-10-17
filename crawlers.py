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



# atraves de um nome soma todas as operações feitas naquele nome
def target_send_transactions(list_of_transactions, owner):
    sum_value = 0
    number = 0
    name = ''
   

    for transaction in list_of_transactions:
        if 'enviada' in transaction['type']:
            if owner in transaction['name']:
                if float(transaction['value']) < 0:
                    sum_value += float(transaction['value'])
                    number += 1
                    name = transaction['name']
    
        target_transactions_info = {
            'name': name,
            'number_of_operations': number,
            'sum_of_target_operation': sum_value
        }
    
    return target_transactions_info

def target_recived_transactions(list_of_transactions, owner):
    sum_value = 0
    number = 0
    name = ''
   
    for transaction in list_of_transactions:
        if 'recebida' in transaction['type']:
            if owner in transaction['name']:
                if float(transaction['value']) > 0:
                    sum_value += float(transaction['value'])
                    number += 1
                    name = transaction['name']
    
        target_transactions_info = {
            'name': name,
            'number_of_operations': number,
            'sum_of_target_operation': sum_value
        }
    
    return target_transactions_info


