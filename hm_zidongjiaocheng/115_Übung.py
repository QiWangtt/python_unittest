# _*_ coding: utf-8 _*_
# @Time: 29.08.2024 10:04
# @Author: Qi Wang
# @File: 115_Übung
# @Project: python_unittest
# Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

func1 = lambda a, b: a * b
print(func1(1, 2))

# parameter is dict
func2 = lambda x: x.get('age')
func3 = lambda x: x['age']

my_dict = {'name': 'Jack', 'age': 18}
print(func2(my_dict))
print(func3(my_dict))

'''# 无参无返回值
def func1():
    print('Hello World')

func1()
# lambda : print('Hello World') # 匿名函数的定义
func11 = lambda: print('Hello lambda')
func11() # 匿名函数的调用， 一般不调用，这里是为了查看

# 无参有返回值
def func2():
    return 10

print(func2())

func22 = lambda: 10
print(func22())

# 有参无返回值
def my_sum(a, b):
    print(a + b)

my_sum(1, 2)
my_sum11 = lambda a, b: print(a + b)
my_sum11(10, 20)

# 有参有返回值
def func4(a, b):
    return a + b

print(func4(1, 2))
func44 = lambda a, b: a + b

print(func44(10, 20))'''
