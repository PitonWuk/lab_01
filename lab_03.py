"""
Завдання 3
 Завдання для функторів. Створіть клас TextModifier,
який може здійснювати різні операції над текстом:
• Операція перетворення тексту у верхній регістр.
• Операція перетворення тексту у нижній регістр.
• Операція видалення пробілів у тексті.
• Операція шифрування тексту за допомогою зсуву
вліво на задану кількість символів.
"""
class TextModifier:
    def __init__(self, text):
        self.text = text

    def __call__(self, operation):
        return operation(self.text)

def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()

def remove_spaces(text):
    return text.replace(" ", "")

def encrypt_shift(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_text += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 +
                                  ord('a' if char.islower() else 'A'))
        else:
            encrypted_text += char
    return encrypted_text

text = "Hello, World!"

modifier = TextModifier(text)

modified_text = modifier(uppercase)
print("Uppercase Text:", modified_text)

modified_text = modifier(lowercase)
print("Lowercase Text:", modified_text)

modified_text = modifier(remove_spaces)
print("Text without Spaces:", modified_text)

modified_text = modifier(lambda x: encrypt_shift(x, 3))
print("Encrypted Text:", modified_text)
