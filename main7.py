#лямбда функция
# def hello(x):
#     return x * x
# print(hello(10))
# ###########.
# hello = lambda x: x * x
# print(hello(10))
# #########
# print((lambda x : x * x)(10))
# #########################
# def mult(num1 : int = 2, num2 : int = 2) -> int:
#     return num1 * num2
# print(mult(10,5))
# print(mult())
####################
# lambda_mult = lambda num1, num2: num1 *num2
# print(lambda_mult(10,5))
###########################
# print((lambda num1,num2: num1 * num2)(10,5))
######################
number = [10,2 ,3 ,4 ,11,12, 100,101]
chet = []
def chet_fuck(num : list) -> list:
    for i in num:
        if i % 2 ==0:
            chet.append(i)
    return chet
print(chet_fuck(number))
########################
# number = [10,2 ,3 ,4 ,11,12, 100,101]
# lambda_chet = list(filter(lambda num : num % 2 == 0, number))
# print(lambda_chet)
###############################
# number = [10,2 ,3 ,4 ,11,12, 100,101]
# print(list(filter(lambda num : num % 2 == 0, number)))
#########################################
# print(list(filter(lambda num : num % 2 == 0, [10,2 ,3 ,4 ,11,12, 100,101])))
####################################
# num = [10, 20 , 30 ,40 ,50]
# lst = []
# def mult(num_list: list) -> list:
#     for i in num_list:
#         lst.append(i * 2)
#     return lst
# print(mult(num))
#########################
# num = [10, 20 , 30 ,40 ,50]
# lst = list(map(lambda num_list: num_list * 2, num))
# print(lst)
###################
# num = [10, 20 , 30 ,40 ,50]
# print(list(map(lambda num_list: num_list * 2, num)))
#########################
# print(list(map(lambda num_list: num_list * 2, [10, 20 , 30 ,40 ,50])))
################################
# import time
# def get_time():
#     return time.ctime()
# # print(get_time())
# ############
# def hello():
#     return "hello world"
# ##################
# it = "GeekTech"
############
number = [10,2 ,3 ,4 ,11,12, 100,101]
chet = []
