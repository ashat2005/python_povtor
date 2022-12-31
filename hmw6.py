
# def a(b):
#     c = b.title().split()
#     for i in range(len(c)):
#         print(c[i][0], end='')
# a('Кыргызстан Республика апр')
#####################
# s = {}
# def a(b):
#     c = b.lower().split(' ')
#     for i in c:
#         s[i] = c.count(i)
# a("Money, money, money, it’s always sunny, in the richmen’s world")
# print(s)
#######################
def a(w):
    b1 = list(w)
    b2 = set(w)
    if len(b1) == len(b2):
        return True
    return False
print(a(""))
####################
# def a(w):
#     return int(str(w)[::-1])
# print(a(123))
###########################
# def bot():
#     while True:
#         wodyt = input("Говорите с нашим ботом: ")
#         for i in wodyt:
#             if i == "?":
#                 print("Конечно!")
#         for i in wodyt:
#             if i == "!":
#                 print("Успокойся")
#         if wodyt == " ":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("ну и что")
# bot()
##########################
def chatbot():
    while True:
        text=input("Введите что-то:")
        if text.find("?")>=0:
            print("Конечно!")
        elif text.find("!")>=0:
            print("Успокойся")
        elif text == "":
            print("Как классно, когда ты молчишь. Продолжай в том же духе!")
        else:
            print("Ну и что")
chatbot()
