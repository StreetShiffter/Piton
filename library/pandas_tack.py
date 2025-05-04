import pandas as pd

# listing = pd.read_csv('..\data\winemag-data-130k-v2.csv')
# print(listing.head(14))

# listing = pd.read_excel('..\data\winemag-data-130k-v2.xlsx', index_col=7)
# print(listing.head(3))

listing = pd.read_excel('..\data\winemag-data-130k-v2.xlsx')
test = listing.set_index('title')
print(test)

# def get_cards_with_spend(sort_period: pd.DataFrame) -> list[dict]:
#     """
#     Функция принимает DataFrame и возвращает список карт с расходами.
#     Возвращает полные номера карт (без звёздочек) и положительный кэшбэк.
#     """
#         transactions_cards = []
#
#         # Убедимся, что суммы - числа
#         sort_period["Сумма операции"] = pd.to_numeric(sort_period["Сумма операции"], errors="coerce")
#         sort_period["Сумма операции с округлением"] = pd.to_numeric(
#             sort_period["Сумма операции с округлением"], errors="coerce"
#         )
#
#         card_sort = sort_period[["Номер карты", "Сумма операции", "Кэшбэк", "Сумма операции с округлением"]]
#
#         for _, row in card_sort.iterrows():
#             if row["Сумма операции"] < 0:
#                 # Получаем полный номер карты без звёздочек
#                 last_digits = str(row["Номер карты"]).replace("*", "")
#
#                 total_spent = row["Сумма операции с округлением"]
#
#                 # Кэшбэк берём из колонки "Кэшбэк" как положительное число
#                 cashback = abs(float(row["Кэшбэк"]))
#
#                 transactions_cards.append(
#                     {
#                         "last_digits": last_digits,
#                         "total_spent": total_spent,
#                         "cashback": cashback,
#                     }
#                 )
#     return transactions_cards
