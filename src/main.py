import re


def clear_name_file(file_name: str) -> list:
    "Функция очистки лишних символов"
    new_list = []

    with open("data/" + file_name, encoding="utf-8") as name_file:
        names_list = name_file.read().split()
        for name_item in names_list:
            cleaned_item = re.sub("[^а-яА-ЯёЁa-zA-Z]", "", name_item)
            if cleaned_item:  # Проверка, что результат не пуст(true или false)
                if len(cleaned_item) > 1:
                    new_list.append(cleaned_item)
    return new_list


def sort_cyrilyc_name(names: str)-> list:
    "Функция вывода имен на кирилице"
    list_name_rus = []

    for name in names:
        cleaned_item = re.sub("[^а-яА-ЯёЁ]", "", name)
        if cleaned_item:
            list_name_rus.append(name)
    return list_name_rus


def sort_latyn_name(names: str)-> list:
    "Функция вывода имен на латыни"
    list_name_eng = []

    for name in names:
        cleaned_item = re.sub("[^a-zA-Z]", "", name)
        if cleaned_item:
            list_name_eng.append(name)
    return list_name_eng

def save_file_data(file_name:str, data:str)->None:
    '''Сохраняет данные в файл'''
    with open("data/" + file_name, 'w', encoding="utf-8") as name_file:
        name_file.write(data)




if __name__ == "__main__":

    start = clear_name_file("name.txt")
    russian_names = sort_cyrilyc_name(start)
    english_names = sort_latyn_name(start)

    save_file_data('rus_name.txt', ' '.join(russian_names))
