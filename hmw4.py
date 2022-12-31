
# it_company = ('Google', 'Amazon', 'Microsoft')
# tup_cities = tuple(it_company)
# print(tup_cities)
# lct_citise = list(tup_cities)
# lct_citise.append('Tesia')
# tup_cities = tuple(lct_citise)
# print(tup_cities)

# it_company = ('Coogle', 'Microsoft', 'Tesia)
# tup_citise = tuple(it_company)
# print(tup_citise)
# lct_citise = list(tup_citise)
# lct_citise.append('Amazon')
# tup_citise = tuple(lct_citise)
# print(tup_citise)

# it_company = ('google', 'amazon', 'microsoft')
# tup_company = tuple(it_company)
# print(tup_company)
# lst_company =  list(tup_company)
# print(lst_company)
# lst_company[0] = 'apple'
# tup_company = tuple(lst_company)
# print(tup_company)

# text_tuple = ['Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'python', 'overview']
# print(text_tuple.count("python"))

# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd':600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

numbers =numbers = {'num_1' : 1, 'num_2' : 2,'num_3' : 3, 'num_100' : 100}
numbers['num_1'] = 1 * 5
numbers['num_2'] = 2 * 5
numbers['num_3'] = 3 * 5
numbers['num_100'] = 100 * 5
print(numbers)

# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] = 17 * 2
# print(student)

# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = 16
# print(student)
 
# student = {'name' : 'Askhat', 'age' : 17}
# student.pop("age")
# print(student)

# student = {'name' : 'Askhat'}
# student.setdefault('address', 'Западный Анар')
# print(student)


# parol = {}
# while True:
#     frist_parol = input("введите пароль: ")
#     posledov_1 = frist_parol.find("123")
#     posledov_2 = frist_parol.find("qwe")
#     if len(frist_parol) > 7:
#         if posledov_1 < 0 and posledov_2 < 0:
#             parol.setdefault('first_p', frist_parol)
#             proverka_paroly = input("введите повторный пароль:")
#             if parol['first_p'] == proverka_paroly:
#                 print("ok")
#             else:
#                 print("различаються")
#         else:
#             print("простой пароль")
#     else:
#         print("короткий пароль")
#     print(parol)

# contact = ["Askhat"]
# while True:
#     command = input("1-посмотреть контакт, 2-добавить в контакты, 3-удалить контакты, 4-обновить контакт")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         app_contact = input("Введите имя: ")
#         contact.append(app_contact)
#         print("Удачно добавлен")
#     elif command == "3":
#         pop_contact = input("Введите имя человека которого хотите удалить: ").title()
#         if pop_contact in contact:
#             contact.remove(pop_contact)
#             print("контакт удален")
#         else:
#             print("контакт не найден")
#     elif command == "4":
#         star_name = input("Введите старое имя: ")
#         new_name = input("Введите новые имя: ")
#         try:
#             contact[contact.index(star_name)] = new_name
#             print("контакт обновлен")
#         except ValueError:
#             contact.append(new_name)
#             print("был создан новый контак")
#     else:
#         print("err")
#         break
