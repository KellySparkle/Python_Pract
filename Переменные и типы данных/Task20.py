# Пользователь вводит пароль. Проверь, что он длиннее 8 символов и содержит хотя бы одну цифру.э
password = input("Введите пароль: ")
print(len(password) > 8 and any(ch.isdigit() for ch in password))