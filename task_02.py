"""
Завдання 2
Створіть дескриптор для атрибуту, що зберігає
розмір файлу. Додайте можливість зберігати розмір
файлу в байтах, але представляти його у зручному для
читання форматі (наприклад, КБ або МБ).
"""
class FileSizeDescriptor:
    def __get__(self, instance, owner):
        return instance._size_in_bytes

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError("The file size must be a number.")
        if value < 0:
            raise ValueError("The file size cannot be negative.")
        instance._size_in_bytes = value

class File:
    size = FileSizeDescriptor()

    def __init__(self, size_in_bytes):
        self.size = size_in_bytes

    def get_formatted_size(self, unit='MB'):
        units = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}
        if unit not in units:
            raise ValueError("Unsupported unit format.")
        size_in_unit = self._size_in_bytes / units[unit]
        return f"{size_in_unit:.2f} {unit}"

file = File(size_in_bytes=1024**2)

print(file.size)

formatted_size = file.get_formatted_size(unit='KB')
print(formatted_size)
