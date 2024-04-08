def output_text(text):
    """
        Функція для виводу тексту у консоль.

        Args:
            text (str): Текст, який буде виведений у консоль.
        """
    print(text)

def write_to_file_builtin(filename, text):
    """
        Функція для запису тексту до файлу за допомогою вбудованих можливостей Python.

        Args:
            filename (str): Ім'я файлу, у який буде записаний текст.
            text (str): Текст, який буде записаний у файл.

        """
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Текст успішно записано у файл {filename}.")
    except Exception as e:
        print(f"Сталася помилка під час запису у файл {filename}: {e}")
