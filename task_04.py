"""
Завдання 4
Створіть клас FileUtils, який має метод класу
count_lines, який приймає шлях до файлу і повертає
кількість рядків у файлі.
"""
class FileUtils:

    @classmethod
    def count_lines(cls, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                return len(lines)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

file_path = "example.txt"
line_count = FileUtils.count_lines(file_path)

if line_count is not None:
    print(f"Number of lines in {file_path}: {line_count}")

