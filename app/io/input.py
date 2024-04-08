def input_text():
    """
    Функція для введення тексту з консолі.

    Returns:
        str: Введений текст.
    """
    text = input("Введіть текст: ")
    return text

def read_from_file_builtin(filename):
    """
        Функція для зчитування тексту з файлу за допомогою вбудованих можливостей Python.

        Args:
            filename (str): Ім'я файлу, з якого буде зчитано текст.

        Returns:
            str або None: Зчитаний текст або None, якщо файл не було знайдено.
        """
    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None

def read_from_file_pandas(filename):
    """
        Функція для зчитування тексту з файлу за допомогою бібліотеки pandas.

        Args:
            filename (str): Ім'я файлу, з якого буде зчитано текст.

        Returns:
            str або None: Зчитаний текст або None, якщо файл не було знайдено.
        """
    try:
        import pandas as pd
        data = pd.read_csv(filename, header=None)
        text = ' '.join(data[0].tolist())
        return text
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None
