from app.io.input import input_text, read_from_file_pandas, read_from_file_builtin
from app.io.output import output_text, write_to_file_builtin


def main():
    pass

text_input = input_text()
text_builtin = read_from_file_builtin("data/test2.txt")
text_pandas = read_from_file_pandas("data/test3.csv")

output_text(text_input)
output_text(text_builtin)
output_text(text_pandas)

write_to_file_builtin("data/copy1.txt", text_input)
write_to_file_builtin("data/copy2.txt", text_builtin)
write_to_file_builtin("data/copy3.txt", text_pandas)


if __name__ == '__main__':
    main()