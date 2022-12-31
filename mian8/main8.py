# def div(num1: int = 2, num2 : int = 2) -> int:
#     try:
#         return num1 // num2
#     except ZeroDivisionError:
#         return "учи матиматику"
#     except TypeError:
#         return "ты используешь слова"
# print(div(19,"0"))
# def calc():
#     while True:
#         try:
#             num1 = int(input("Введите первое число: "))
#             operator = input("+, -, *, /: ")
#             num2 = int(input("Введите второе число: "))
#             if operator == "+":
#                 print(num1 + num2)
#             elif operator == "-":
#                 print(num1 - num2)
#             elif operator == "*":
#                 print(num1 * num2)
#             elif operator == "/":
#                 try:
#                     print(num1 / num2)
#                 except ZeroDivisionError:
#                     print("деление на ноль")
#             else:
#                 print("Оператор не найден")
#         except ValueError:
#             print("вы вели буквы")
# calc()
# try:
#     print(10 / 2)
# except:
#     print("ошибка")
#     # raise ValueError("специально вызвали ошибку с raise")
# finally:
#     print("я всегда буду работать")
# f = open('hello.txt', 'w')
# f.write('hello1')
# f.close()
# r = open('hello.txt', 'r')
# print(r.read())
# r.close()
# import time
# def save_login_password(login : str, password : str) -> str:
#     password_file = open('login_password.txt', 'a+')
#     if login and len(password) >= 8 and ' ' not in password:
#         password_file.write(f"{login},{password},{time.ctime()}\n") 
#     else:
#         return "неправельный логин или пароль"
#     password_file.close()
#     return "логин и пароль сохранен"
# print(save_login_password("", "askhat2022"))
# print(save_login_password("askhat", "geekcoin"))
# print(save_login_password("nurbolot", "geekcoin2"))
# print(save_login_password("nurbolot", "         "))
# with open('geek.txt', 'a+') as g:
#     g.write('hello\n')
#     g.write('dasd\n')
#     g.write('asddadasdd\n')
#     g.write('heladlo\n')
# with open('geek.txt', 'r') as r:
#     print(r.read())

import random
import time
def randomayzer():
    return random.randint(1,10)
def user_contact(name: str, number: str, secret_key: str):
    with open('wins.txt', 'a+', encoding='utf-8') as win:
        win.write(f"имя: {name}, номер: {number}, ключ: {secret_key}, дата: {time.ctime()}\n")
def main():
    random_number = randomayzer()
    n = 0
    while True:
        user_input = int(input("Введите любое число: "))
        n += 1
        if random_number == user_input:
            print("вы выйграли! Введи свои данные для контакта")
            name = input("Введите свое имя: ")
            number = input("Введите свой номер: ")
            secret_key = input("Введите свое секретное слово: ")
            user_contact(name,number,secret_key)
            print("ваши данные записа   ны")
            break
        else:
            print(f"вы проиграли {5 - n} попыток")
            if 5 - n == 0:
                break
main()
