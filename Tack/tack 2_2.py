from typing import List


def palindroms_list(nums: List[int]) -> List[int]:
    """Функция которая ищет палиндромы"""
    list_palindrome = []
    for i in nums:
        # Преобразуем число в строку и проверяем, является ли оно палиндромом
        if str(i) == str(i)[::-1]:
            list_palindrome.append(i)
    return list_palindrome


if __name__ == "__main__":
    print(palindroms_list([121, 123, 131, 34543]))
