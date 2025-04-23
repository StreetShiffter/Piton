import json



# def filter_transaction(func): # Ищем транзакции и добавляем в пустую функцию
#     def choise(*args, **kwargs):
#         with open('transactions.json') as f:
#             data = json.load(f)
#         result = func(*args, **kwargs)
#         filtered_transactions = []
#         for transaction in data:
#             if transaction["amount"] >= 1000:
#                 filtered_transactions.append(transaction)
#         return filtered_transactions
#     return choise
#
# @filter_transaction
# def list_transaction():
#     return []


def filter_transaction(func):
    def choise(*args, **kwargs):
        with open('transactions.json') as file: # Открываем исходный файл
            data = json.load(file)
            result = func(*args, **kwargs) # Открываем фильтрованную функцию
            total_amount = sum([transaction['amount'] for transaction in result]) # Суммируем транзакции на сумму [1000, -20]
            statistic = f'Отфильтровано {len(result)} из {len(data)} результата на сумму {total_amount}'
            return statistic

    return choise


@filter_transaction
def filter_transactions_by_currency(input_list, currency):# получаем JSON файл и желаемое значение для фильтрации
    with open(input_list) as file:
        data = json.load(file)

    transaction_cur = [trans for trans in data if trans['currency'] == currency]

    with open('transactions_usd.json', 'w') as f: #На всякий случай записываем результат
        json.dump(transaction_cur, f)

    return transaction_cur


input_file = 'transactions.json'
currency = 'USD'

filtered_transactions = filter_transactions_by_currency(input_file, currency)
print(filtered_transactions)
