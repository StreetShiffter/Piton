from mocking_testing.greeting import get_greeting
from unittest.mock import patch


# Вариант 1: Тесты с контекстным менеджером with patch()

def test_morning_greeting_with_context():
    """Тест утра с использованием контекстного менеджера"""
    with patch('mocking_testing.greeting.datetime.datetime') as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.hour = 8  # 8 утра

        result = get_greeting()
        assert result == "Доброе утро!"
        mock_datetime.now.assert_called_once()


def test_afternoon_greeting_with_context():
    """Тест дня с использованием контекстного менеджера"""
    with patch('mocking_testing.greeting.datetime.datetime') as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.hour = 14  # 14 дня

        result = get_greeting()
        assert result == "Добрый день!"
        mock_datetime.now.assert_called_once()


def test_evening_greeting_with_context():
    """Тест вечера с использованием контекстного менеджера"""
    with patch('mocking_testing.greeting.datetime.datetime') as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.hour = 20  # 20 вечера

        result = get_greeting()
        assert result == "Добрый вечер!"
        mock_datetime.now.assert_called_once()


# Вариант 2: Тесты с декоратором @patch

@patch('mocking_testing.greeting.datetime.datetime')
def test_morning_greeting_with_decorator(mock_datetime):
    """Тест утра с использованием декоратора"""
    mock_now = mock_datetime.now.return_value
    mock_now.hour = 8

    result = get_greeting()
    assert result == "Доброе утро!"
    mock_datetime.now.assert_called_once()


@patch('mocking_testing.greeting.datetime.datetime')
def test_afternoon_greeting_with_decorator(mock_datetime):
    """Тест дня с использованием декоратора"""
    mock_now = mock_datetime.now.return_value
    mock_now.hour = 14

    result = get_greeting()
    assert result == "Добрый день!"
    mock_datetime.now.assert_called_once()


@patch('mocking_testing.greeting.datetime.datetime')
def test_evening_greeting_with_decorator(mock_datetime):
    """Тест вечера с использованием декоратора"""
    mock_now = mock_datetime.now.return_value
    mock_now.hour = 20

    result = get_greeting()
    assert result == "Добрый вечер!"
    mock_datetime.now.assert_called_once()
