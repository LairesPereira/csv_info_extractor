import csv

# nubank_outubro_2023.csv

# listando todas as transações
# abrir o arquivo como objeto
# para cada linha imprimimos apenas a informação relevante

def getTransactionsInfo():
    with open('./csv_files/nubank_outubro_2023.csv', 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        final_list = []
        for line in csv_reader:
            if('Boleto' in line['Descrição']): continue
            elif('fatura' in line['Descrição']): continue
            else:
                transaction_info = {
                    "date": line['Data'],
                    "type": line['Descrição'].split('-')[0].lower(),
                    "name": line['Descrição'].split('-')[1].lower(),
                    "value": line['Valor'],
                }
                final_list.append(transaction_info)    
        return final_list


