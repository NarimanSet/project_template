def output_text(text):
    """Функція для виводу тексту у консоль."""
    print(text)

def write_to_file_builtin(filename, text):
    """Функція для запису тексту до файлу за допомогою вбудованих можливостей Python."""
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Текст успішно записано у файл {filename}.")
    except Exception as e:
        print(f"Сталася помилка під час запису у файл {filename}: {e}")
