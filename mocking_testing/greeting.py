import datetime


def get_greeting():
    hour = datetime.datetime.now().hour

    if 5 <= hour < 12:
        return "Доброе утро!"
    elif 12 <= hour < 18:
        return "Добрый день!"
    else:
        return "Добрый вечер!"

print(get_greeting())