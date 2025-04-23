from typing import Union
import logging

loger_func = logging.getLogger('111111')  # логер к текущему модулю
file_handler = logging.FileHandler('../logs/example.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s\n')
file_handler.setFormatter(file_formatter)
loger_func.addHandler(file_handler)
loger_func.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция, которая маскирует предпоследние 6 цифр"""
    card_number = str(number_card).replace(" ", "")
    if not card_number.isdigit():  # Проверка на числовое значение
        loger_func.error("%s", number_card)
        raise ValueError("Введите числовое значение")

    if len(card_number) == 16:  # Маскировка для 16 символов
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        loger_func.info("Успешная маскировка номера карты: %s", masked_number)
        return masked_number

    elif len(card_number) == 21:  # Маскировка для 21 символа
        masked_number = f"{card_number[:11]}******{card_number[-4:]}"
        loger_func.info("Успешная маскировка номера карты: %s", masked_number,)
        return masked_number
    else:
        loger_func.error("%s", number_card)
        raise ValueError("Неверный номер карты! Введите 16 или 21 символ.")


test0 = "1230 8520 9632 74122"
get_mask_card_number(test0)
