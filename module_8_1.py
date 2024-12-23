def add_everything_up(a, b):
    try:
        # Пробуем преобразовать оба значения в float для сложения
        return float(a) + float(b)
    except ValueError:
        # Если возникла ошибка преобразования, возвращаем строковое представление
        return str(a) + str(b)
    except TypeError as exc:
        print(f"Ошибка: {exc}. Не удалось сложить {a} и {b}.")
        return None

# Тестовые вызовы функции
print(add_everything_up(123.456, 'строка'))  # Ожидается: 123.456строка
print(add_everything_up('яблоко', 4215))  # Ожидается: яблоко4215
print(add_everything_up(123.456, 7))  # Ожидается: 130.456
print(add_everything_up([1, 2], 'строка'))  # Ожидается: ошибка сложения