def input_text():
    """Функція для введення тексту з консолі."""
    text = input("Введіть текст: ")
    return text

def read_from_file_builtin(filename):
    """Функція для зчитування тексту з файлу за допомогою вбудованих можливостей Python."""
    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None

def read_from_file_pandas(filename):
    """Функція для зчитування тексту з файлу за допомогою бібліотеки pandas."""
    try:
        import pandas as pd
        data = pd.read_csv(filename, header=None)
        text = ' '.join(data[0].tolist())
        return text
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None
