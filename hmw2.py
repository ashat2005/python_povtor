
# login = "askhat"
# password = "123"
# user_login = input("Введите имя: ")
# user_password = input("Введите пароль: ")
# if user_login == login and user_password == password:
#     print("Password is correct. You arewelcome")
# elif user_login != login and user_password != password:
#     print("Password is incorrect. Please, try again")
# else:
#     print("err")


# if operator >= "-30" and operator <0:
#    print("При условии меньше -30 градусов: ")
# elif operator >= 0 and operator<15:
#     print("Холодновато.Оденься потеплее!")
# elif  operator >= 15 and operator<30:
#     print("Прохладно.Куртку накинь!")
# elif operator >= 30 and operator<50:
#     print("Тепло.Иди погуляй в парке!")
# elif operator <=50:
#     print("Ого,жарко!")

operator = int(input("-30, 0, 15, 30, 50"))
if operator >= -30 and operator <0:
   print("При условии меньше -30 градусов: ")
elif operator >= 0 and operator<15:
    print("Холодновато.Оденься потеплее!")
elif  operator >= 15 and operator<30:
    print("Прохладно.Куртку накинь!")
elif operator >= 30 and operator<50:
    print("Тепло.Иди погуляй в парке!")
elif operator <=50:
    print("Ого,жарко!")

name = "Advertising companies say advertising is necessary and important. It informs people aboutnew products. Advertising hoardings in the street make our environment colourful. Andadverts on TV are often funny. Sometimes they are mini-dramas and we wait for the nextprogramme in the mini-drama. Advertising can educate, too. Adverts tell us about new,healthy products. And adverts in magazines give us ideas for how to look prettier, befashionable and be successful. Without advertising, life is boring and colourless.But some consumers argue that advertising is a bad thing. They say that advertising is badfor children. Adverts make children pester their parents buy things for them. Advertisersknow we love our children and want to give them everything. So they use childrens pesterpower’ to sell their products. Finally, consumers say, if there is advertising there must berules. Some adverts advertise unhealthy things like cigarettes and make people waste theirmoney"
print(name.count("s"))
print(name.count("t"))

# name = "aidana"
# name_2 = "adilet"
# print((name[0] + name_2[0]) + (name[1] + name_2[1]) + (name[2] + name_2[2]) + (name[3] + name_2[3]) + (name[4] + name_2[4]) + (name[5] + name_2[5])) 
