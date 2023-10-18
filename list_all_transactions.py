import csv

def getTransactionsInfo(file_path):
    with open('csv_files/' + file_path, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        final_list = []
        for line in csv_reader:
            if('Boleto' in line['Descrição']): continue
            elif('fatura' in line['Descrição']): continue
            elif('recarga') in line['Descrição'].lower(): continue
            else:
                transaction_info = {
                    "date": line['Data'],
                    "type": line['Descrição'].split('-')[0].lower(),
                    "name": line['Descrição'].split('-')[1].lower(),
                    "value": line['Valor'],
                }
                final_list.append(transaction_info)    
        return final_list


