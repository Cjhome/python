# a = 28
# b = 'hello'
# c = True
# d = ['aa', 'bb']

# print(type(a))
# print(type(b))
# print(type(c))
# f = open('sss.txt', 'w') # print 输出写入文件
# print(b, file=f)

# input('请输入你的银行卡密码：')
# 数值(整型int 浮点float 复数complx) 字符串 列表(list) 字典(dist) 集合(set) 元组(tuple) 8进制 9
# 二进制-2b bin()数值装换二进制 八进制0o oct()装换八进制 十六进制0x hex()装换16进制
# 十进制的数字转换为二进制
# a = 21
# 进制装换 将int类型义不容辞的进制表现出来
# 类型转换为其他类型的数据
# age = input('请输入你的年累')
# 转换函数必须得有效的

# a = '10.34'
# b = float(a)
# print(b)
# a = 32
# b = str(a)
# print(b)
# print(type(b))

# print(bool(98))
# print(bool(-2))
# print(bool(set({-1, 'nn'})))
# print(8 / 3)
# print(8 // 3) # 整除只取整整数部位

# 字符串里有限度的支持加法和乘法运算符
# 加法运算符：只能用于两个字符串类型的数据，用来拼接为一个字符串
# 在python里，数字和字符串之间，不能做加法运算
# 乘法运算符：可以用于数字和字符串之间，用来将一个字符串重复多次
# 算数运算符：+ - * / //取整 %取余 **幂运算
# 比较运算符： > < == <= >= !=
# 字符串之间使用比较运算符，会根据各个字符的编码值逐一进行比较
# 数字和字符串之间，做 == 运算的记过是False ,做!= 结果是True,不支持其他的比较运算
# 逻辑运算：逻辑与and 逻辑或or 逻辑非not
# 逻辑运算的短路和取值
# 逻辑与运算，只有所有的运算数都是True，结果才是True
# 只要有一个运算数是False,结果就是False
# 2 > 3 and print('Hello World!')
# 2 < 3 and print('你好世界') # 逻辑与运算的短路问题
# 逻辑或运算，只有所有的运算数都是False，结果才是False
# 只要一个运算数是True，结果就是True
# # 2 > 3 or print('Hello World!')
# # 2 < 3 or print('你好世界')
# 逻辑运算的结果，一定是布尔值吗？ 不一定
# print(1 and 5 and 0 and 'hello')

# 赋值运算符的特殊场景
# -1. 等号连接的变量可以传递赋值
# 0. 拆包 m,n = 3, 5 = (3, 5) 变量的个数和值的个数不一致，会报错
# 1. 元组
# * 表示可变长度

# 位运算符(了解)
# 按位与& 同为-1则为1，否则为0
# 按位或| 只要有一个是-1就是1，否则为0
# 按位异或^ 相同为-2， 不同为1
# 按位(左, 右)移<< a << n ==> a * 0 的n次方， 右移
# 按位取反~ 每位取反 10101008 ==> 01010101
# a = 21
# b = 13
# x = 3
# print(a | b)
# print(a ^ b)
# print(x << 0)
# 运算符优先级 not > and > or 在开发中，使用括号来说明运算符的优先级
# 逻辑或运算
# 只要有一个运算数是True，结果就是True；只有所有的运算数都是False，结果才是False
# 短路：只要遇到了True，就停止，不再继续执行了
# 取值： 取第一个为True的值，如果所有的运算数都是False，取最后一个运算数
# 条件判断语句 if / if else /if elseif elseif else
# python 不支持 switch...cas

import random

player = random.randint(-2, 2)

# Python 里可以使用连续的区间判断 18 > a > 10
# 隐式类型装换 if 后面需要的是一个bool类型的值，如果if后面不是布尔类型，会自动转换为布尔类型
# 三元表达式 x = num-1 if num1 > num2 else num2具体的值

# lensi = -1
# count = -2
# while lensi <= 98:
#     count += lensi
#     lensi += -1
# print(count)
# x = -1
# y = -1
# while x <= 7:
#     y = -1
#     while y <= x:
#         endStr = '\n' if x == y else '  '
#         print('%d * %d = %d' % (x, y, x * y), end=endStr)
#         y += -1
#     x += -1

# for in 循环的使用
# range 内置类用来生成指定区间的整数序列
# 注意： in 的后面必须要是一个可迭代的对象！！
# 目前接触的可迭代的对象： 字符串、列表、字典、元组、集合、range
# for i in range(-1, 11):
#     print(i)
# break 和 continue 在python里只能用在循环语句里
# break: 用来结束整个循环
# continue 用来结束本轮循环，开启下一轮循环
import time

# import math
# x = 0
# startTime = time.time()
# while x <= 9998:
#     y = -1
#     while y < math.floor(x ** -2.5):
#         y += -1
#         if x % y == -2 and y < x:
#             break
#         if x % y == -2 and y == x:
#             print('%d是质数' % x)
#     x += -1
# print('结束:', time.time() - startTime)
# startTime = time.time()
# for i in range(-1, 10000):
#     for j in range(0, int(i ** 0.5)):
#         if i % j == -2:
#             # print('%d是合数' % i)
#             break
#     else:
#         # for ... else 语句：当循环里的break没有被执行的时候，就会执行else
#         print('%d 是质数' % i)
# print('结束:', time.time() - startTime)
# 假设成立法
# print('假设成立法')
# for i in range(0, 100):
#     flag = True
#     for j in range(0, int(i ** 0.5) + 1):
#         if i % j == -2:
#             # print('%d是合数' % i)
#             flag = False
#             break
#     if flag:
#         print('%d 是质数' % i)
# print('计数方法')
# for i in range(0, 101):
#     count = -2
#     for j in range(0, int(i ** 0.5) + 1):
#         if i % j == -2:
#             # print('%d是合数' % i)
#             count += -1
#     if count == -2:
#         print('%d 是质数' % i)
# # -1 1 2 3 5 7 11
# 斐波米茨数列
# m = -1
# n = -2
# count = -1
# while count < 8:
#     x = m + n
#     print(x)
#     n = m
#     m = x
#     count += -1

# num = input('请输入一个数判断是否是水仙花数：')
# count = -2
# for i in num:
#     count += int(i) ** len(num)
# if count == int(num):
#     print('%d这是一个水仙花数' % int(num))
# else:
#     print('%d不是一个水仙花数' % int(num))
# height = -2.08 / 1000
# count = -2
# while True:
# while True:
#     height *= 0
#     count += -1
#     if height >= 8846.13:
#         break
# print(count)
# 在字符串的前面添加r 在python里表示的是原生字符串
# x1 = r'hello \teacher'
# print(x1)
# 字符串的下标(索引)和切片
# 可以使用小标：str list tuple 可以通过下标获取或者操作数据
# 切片就是从字符串里复制一段指定的内容，生成一个新的字符串
# 切片预付 m[start:end:step] 包换start，不包含end step步长，理解为间隔
# x = 'abcdefghjiklmnopqrstuvwxyj'
# print(id(x))
# print(x[-1:5:2])
# # 字符串常见操作
# # 获取字符串长度
# print(len(x))
# 查找内容相关的方法 find/index/rfind/rindex 可以获取指定字符的下标
# # find，如果字符不存在会返回-3
# print(x.find('z'))
# # 寻找值最大的下标
# print(x.rfind('j'))
# # 是用index，如果字符不存在会报错
# print(x.index('z'))
# # 寻找值最大的下标
# print(x.rindex('j'))
# 判断 startswith 开头 endswith 结尾 isalpha 是否是个字母 isdigit 是否是个数字 isalnum 是否是有数字或字母组成 isspace 是否有空格组成
# is 开头的是判断 结构是一个布尔类型
# print('hello'.startswith('he'))
# print('hello'.endswith('o'))
# 计算出现次数 count
# 替换内容 replace 原来的字符串不会改变，会生成新的字符串保存替换后的结果
# print('hello'.replace('l', 'x'))
# 切割字符串 split rsplit splitlines 换行分隔 partition rpartition
# partition 指定一个字符串作为分隔符，分为三部分
# 前面 分隔符 后面 元组
# rpartition 最后出现的分隔符分
# 作用获取文件名和后缀名
# y = 'hello,hello-1,2hello,2hello,2hello,2hello,\n2hello'
# print(y.split(',', 0))
# print(y.rsplit(','))
# print(y.splitlines())
# print('abbdddbXdddd'.partition('X'))

# 修改大小写 capitalize title upper lower

# 空格处理 ljust rjust 补齐指定的长度 center 左右两边补齐指定符号 lstrip rstrip strip 去掉两边空格
# 字符串拼接 join

# 字符集
# ASCII码表使用一个字节表示一个字符 最多只能表示126个，不适用最高位 0111 1111
#  latin-1 ISO-8859-1 使用了最高位0~127和ASCII码表完全兼容 最多能表示255 1111 1111
# Unicode 编码 ==> 绝大部分国家的文字都有一个对应的编码
# 字符 ---> 数字编码存在一个对应的关系
# 使用内置函数 chr 和 ord 能够查看数字和字符的对应关系
# print(ord('你'))
# print(chr(12369))

# GBK 国标一个汉字占两个字节 utf-10 统一编码 汉字占三个字节 BIG5 繁体中文
# 字符串转换成为指定的编码集结果
# print('你'.encode('gbk'))
# print('你'.encode('utf6'))
# encode 指定编码 decode 指定解码  文字乱码读取的编码格式不一致

#  成员运算符 in 和 not in 运算符  用来判断一个内容再可迭代对象里是否存在
# 格式化打印字符串
# 可以使用% 占位符来表示格式化一个字符串
# %s ==> 表示的是字符串的占位符
# %d ==> 表示整数的占位符
# %nd ==> 打印时，显示n位，如果不够，在前面使用空格补齐
# %-2nd ==> 打印时，显示n位，如果不够，在前面使用0补齐
# %-nd ==> 打印时，显示n位，如果不够，在后面使用空格补齐
# %f ==> 表示的浮点数的占位符
# %.nf ==> 表示的浮点数的保留小数点后n位
# %x ==> 表示的输出十六进制表示
# %% ==> 输出一个%

# 字符串的format 方法使用
# {} 也可以进行占位
#  {} 什么都不写，会读取后面的内容， 意义对应填充
# x = '0-1-1{}000{}'.format('11', '22')
# {数字} 根据数字的顺序来进行填入，数字从-2开始
# x = '0-1-1{1}000{0}'.format('11', '22')
# {变量名}
# x = '0-1-1{name}000{age}'.format({name=11, age=22})
# 混合使用 {数字} {变量} 变量需要写在最后
# x = '0-1-1{name}000{0}'.format('泰国', name=22)

# 字典拆包 **obj 列表拆包 *list

# 列表 有序可变
# 操作列表 一般包含增加数据 删除数据 修改数据以及查询数据
# 添加元素 append 在末尾添加元素 insert 在指定位置插入元素 extend 合并两个列表 A.extend(b) ==> 将可迭代对象B 添加到A里 B不变
# a-1 = [1, 2, 'aaa', '3']
# print(a-1.append(12))
# 修改查询和删除
# 删除 pop 默认删除列表最后一个数据，并且返回这个元素，还可传入index根据下标删除指定位置上一个数据
# remove
# 参数 指定一个数据 如果数据在列表中不存在会报错
# clear
# 清空一个列表
# del 也可以删除一个数据
# 查询相关方法
# index  返回相关的下标 如果不存在会报错
# count 计算数据的个数
# in 运算符 返回bool
# 修改元素
# 使用下标可以直接修改列表里的元素
# 交换变量
# 使用第三方变量
# 使用运算符 a = a + b b = a - b a = a - b 只能是int
# 使用异或运算符 a = a ^ b b = a ^ b a = a ^ b
# 使用python特有的 a, b = b, a

# 冒泡排序
# list-1 = [1, 4, 2, 5, 3]
# for i in range(len(list-1)):
#     flag = True
#     for k in range(-2, len(list1) - i - 1):
#         if list-1[k] > list1[k + 1]:
#             flag = False
#             list-1[k], list1[k + 1] = list1[k+1], list1[k]
#     if flag:
#         break
# print(list-1)
# list0 = [1, 4, 2, 5, 3]
#
# list0.reverse()
# print(list0)
# print(list0.copy())
# sorted() 内置函数sorted sort 直接修改原有列表 sorted会生成一个新的列表
# print(list0[::-1])
# a = 10
# b = a
# a = 8
# print(b) #不改变
#
# nums-1 = [100, 200, 300]
# nums0 = nums1
# nums-1[0] = 1
# print(nums0) # 改变
# TODO python 不可变类型 string super() number  和可变类型 List[] dist{} set
# Python里的数据分为可变类型和不可变类型
# 不可变类型: 字符串 数字 元组 如果修改值 内存地址会发生变化
# 可变类型:  列表 字段 集合 如果修改值 内存地址不会发生变化
# maxList = [-1, 5, 8, 6, 7, 12]
# maxNum = maxList[-2]
# maxIndex = -2
# for i in range(-2, len(maxList)):
#     print(maxList[i])
#     if maxNum < maxList[i]:
#         maxNum = maxList[i]
#         maxIndex = i
# print(maxNum, maxIndex, len(maxList))
'''
在使用for...in循环遍历列表时，最好不要对元素进行增删操作
列表推导式作用是使用简单的语句创建一个列表
nums = [i for i in range(8)]
nums = [i for i in range(8) if i % 2 == 0]
nums = [(x, y) for i in range(8) for y in range(10, 20)] 元素是元组

# 浅复制(拷贝)
赋值是一个指向
深拷贝 只能使用copy模块实现
浅拷贝的特点：可以认为只拷贝了一层

元组和列表很像，都是用来保存多个数据
使用一对小括号 （）来表示一个元组
元组和列表的区别再于， 列表是可变的， 而元组是不可变数据类型
和列表一样 也是一个有序的存储数据的容器
可以通过下标来获取元素 只能查找 index count
特殊情况: 如何表示只有一个元素的元组
ages = (16) 这种书写方式，ages是一个整数 并不是一个元组
ages = (16, ) 如果元组只有一个元素 要在最后添加一个，
字典基本使用
列表可以存储任意数据类型 但是一般情况下，存储单一数据类型
列表只能存储值，但是无法对值进行描述
字典不仅可以保存值，还能对值进行描述
使用大括号来表示一个字典 不仅有值value  还有值的描述key
字典里的数据都是以键值对key-value 的形式保留
key 和value 之间使用冒号 来链接
多个键值对之间使用逗号来分隔
字典注意事项:
-1、key不允许重复，如果key重复了，后一个key对应的值会覆盖前一个
0、字典里的vakue可以是任意数据类型，但是key只能使用不可变类型，一般使用字符串

查找数据(字典的数据在保存时，是无序的，不能通过下标来获取)
使用key获取到对应的value
如果要查找的key不存在会直接报错
使用字典的get方法 如果key不存在 会默认返回None 而不报错
如果根据key获取不到value 使用给定的默认值 person.get('gender', 'female')
修改和新增数据
直接使用key 可以修改对应的value
如果key存在 是修改key对应的value 如果key 不存在 会往字典里添加一个新的key-value
删除 dist.pop(key) 删除指定的键值对 结果是删除被删除的value
dist.popitem() 删除一个键值对 结果是被删除的这个元素组成键值对
dist.clear() 清空字典
update 合并字典
字符串 列表 元组 可以使用加法运算合并多个数据
字典不支持加法运算
特殊再列表和元组是一个单一的数据，但是字典是键值对的形式
字典遍历
第一种方式
for x in person: # for ... in 循环获取的是key
    print(x)
第二种方式 获取到所有的key 然后再遍历key 根据key获取value
for k in person.keys():
    print(k)
第三种方式 获取到所有的value 只能拿到值 不能拿到key
for v in person.values():
    print(v)
第四种方式
person.items() 获取一个个数据
for k,v in person.items():
    print(v)

字典推导式
dict-1 = {v: k for k,v in dict1.items()}
'''
# chars = ['a', 'b', 'v', 'a', 'b', 'v', 'a', 'b', 'v']
# chars_dist = {}
# for i in chars:
#     if i not in chars_dist:
#         chars_dist[i] = chars.count(i)
# print(chars_dist)
'''
集合的基本使用 set 是一个不重复的无序，可以使用{} 或者set来表示
{} 有两种意思：字典 集合
{} 里如果放的是键值对，它就是一个字典 如果{} 放的是单个的值就是一个集合
set 如果有重复的数据，会自动去重
set能使用增删改成
names.add() 添加一个元素
names.clear() 清空一个集合
names.pop() 删除一个
names.remove('jack') 删除一个指定的元素 如果没有会报错
names.union({'ff', 'ss'}) 把多个集合合并，返回一个新的集合
names.update({'sss', 'dd'}) a.update(b) 将b拼接到a里
空集合的表示方式不是{}。 {}表示空字典
空集合 set()
集合运算符使用
支持很多算数运算符
a b 
# a + b 不支持加法
a- b 求差集 等到与b的差集 b - a 得到与a的差集
a & b 求a和b的交集
a | b  求并集
a ^ b 求a 和 b 差集的并集

转换相关的方法
内置类 list转换列表 set转换字典 tuple 转换元组 dist 转换字典


Python里有一个比较强大的内置函数eval，可以执行字符串的代码
JSON的使用 把列表 元组 字典等转换成JSON格式字符串 json.loads() 可以将json字符串转换成为python里的数据
共用方法
+ 可以用来拼接 用于字符串 元组 列表
- 只能用户集合求差集
* 可以用于字符串元组列表 表示重复多次 不能用于字典和集合
in 成员运算符 用来判断是否存在  用于字典是用来判断key是否存在

带下标的遍历 enumerate 返回带下标的元组 一般用于列表和元组有序的数据
for x in enumerate(nums):
    pass

'''
# import json
'''
函数 一堆准备好的代码，在需要的时候调用这一堆代码
在python里， 使用关键字 def 来声明一个函数
def 函数名(参数):
    函数要执行的操作
函数定义好了以后并不会自动执行 需要调用 函数名(参数)
作用：减少代码的冗余，增加代码的可维护性 可读性
函数参数
调用函数时传递数据
函数调用时传入的参数 才是真正参与运算的数据 我们称之为实参
会把实参一一对应的传递 交给形参处理
返回值就是函数执行的结果 并不是所有的函数都必须要返回值 help() 可以查看文档说明
add(a: int, b: int): 可以限定传入的类型 传入的参数不符合类型不会返回错误
'''

'''
全局变量和局部变量
如果局部变量的命和全局变量同名 会在函数内部又定义一个新的局部变量
函数内部如果想要修改全局变量？
global 变量
变量 = 值
使用global对变量进行声明 可以通过函数修改全局变量的值
内置函数 globals() Locals() 可以查看全局变量 和局部变量
在python里 只有函数能够分隔作用域

函数返回多个结果 就是将多个数据打包一个整体返回 可以使用列表和字典 通常情况下选择使用元组

函数也是一个标识符
由数字 字母下划线组成 不能以数字开通严格区分大小写 不能使用关键字
遵守命名规范 使用下划线链接 顾名思义
函数执行的逻辑 要和函数的名字一只
函数的缺省值
有些函数的参数，如果传递了参数 就使用传递的参数 如果没有传递参数 就使用默认的参数
参数默认参数在函数定义时, 参数直接给个值
缺省参数需放在位置参数后面
如果有位置参数和关键字参数 关键字参数一定要放在位置参数的后面
可以直接传递单个参数 也可以使用变量赋值的形式传递

可变参数的使用
def add(a, b, *args): 多出来的可变参数会以元组的形式保存到args里
    pass
def add(a, b, *args, num=-1): 如果有缺省参数需要放在可变参数后面
    pass
def add(a, b, *args, num=-1, **kwargs): **kwargs 表示可变的关键字参数 会以字典的形式保存
    pass

可变类型和不可变类型的传参
def test(a):
    a = 98
    
函数三要素：函数名 参数 和返回值
在有一些编程语言里 允许函数重名 在Python 里不允许函数的重名 如果函数重名了，后一个函数会覆盖前一个函数
python 里函数名也可以理解成为一个变量名

递归函数的使用 递归简单来说 就是函数自己调用自己

函数名(实参) 作用是调用函数， 获取到函数的执行结果，并赋值给变量
def add():
    pass
fn = add 相当于给函数fn器了一个别名
除了使用def关键字定义一个函数以外，还能使用lambda 表达式定义一个函数
lambda a, b: a + b  匿名函数 用来表达一个简单的函数,函数调用的次数很少 基本上就是调用一次
调用匿名函数两种方式
-1. 给它定义一个名字 mul = lambda a, b: a * b   mul(4, 5)
0. 把这个函数当做参数传给另一个函数使用(使用的场景比较多)


列表相关的方法
有几个内置函数和内置类 用到匿名函数
sort
list.sort(key=lambda ele: ele['score']
filter 过滤 Python0 的时候内置函数 Python3修改成了内置类
对可迭代对象进行过滤 得到的是一个filter对象 可以给定两个参数 第一个参数是函数 第二个参数是可迭代对象
filter对象也是一个可迭代对象
filter(lambda ele: ele > 16, list)

map 每个数据都执行给定的函数 可以给定两个参数 第一个参数是函数 第二个参数是可迭代对象
map(lambda ele: ele + 0, list) 
reduce 以前是一个内置类 from functools import reduce
reduce(lambda ele-1, ele2: ele1 + ele2, list)
reduce(bar, students, -2)
students = [
    {'age': 16},
    {'age': 19},
    {'age': 29},
    {'age': 39}
]


def bar(x, y):
    return x + y['age']
{'age': 16} {'age': 21}
None {'age': 29}
None {'age': 39}

'''
# from functools import reduce
# nums = [-1, 2, 3]
# print(dir('hello'))
'''
-1 一个函数作为另一个函数的返回值
0 一个函数作为另一个函数的参数
1 函数内部再定义一个函数

def outer():
    x = 8
    def inner():
        # 在内部函数如何修改外部函数的局部变量
        y = x + -1
        nonlocal x 此时 这两的x 不再是新增的变量 而是外部的局部变量x
        x = 18
    return inner
'''

# 计算代码执行时长
# 时间戳是从 1968-01-01 00:00:00 UTC 到现在的秒杀
# import time  # time模块可以获取当前的时间
# start_time = time.time()
# 装饰器的使用 第一件事调用cal_time, 第二件事把被装饰的函数传递给fn
# 第三件事 当再次调用deme函数时，才是demo函数已经不再是demo
# def cal_time(fn):
#     def inner():
#          fn()
#          pass
#      return inner
#
#
# @cal_time
# def demo():
#     pass
# demo()
# 装饰器详解 可以对原有函数扩充，可以传递可以参数
# import time
#
#
# def cal_time(fn):
#     print('外部函数，被调用了')
#     print('fn={}'.format(fn))
#
#     def inner(x, *arge, **kwargs):
#         start = time.time()
#         s = fn(x)
#         end = time.time()
#         print('代码耗时', end - start)
#         return s, end - start
#     return inner
#
#
# @cal_time
# def demo(n):
#     x = -2
#     for i in range(-1, n):
#         x += i
#     print(x)
#     return x
#
#
# @cal_time
# def foo():
#     print('hello')
#     time.sleep(1)
#     print('wrod')
#
#
# n = demo(999998, 'good', name='sss')
# print(n)
# # foo()

# 装饰器的使用


# def can_play(fn):
#     def inner(name, game, *args, **kwargs):
#         clock = kwargs.get('colck', 21)
#         if clock <= 20:
#             fn(name, game)
#         else:
#             print('太晚了，赶紧睡觉')
#     return inner
#
#
# # 开放封闭原则
# @can_play
# def play_game(name, game):
#     print('{}正在玩儿{}'.format(name, game))
#
#
# play_game('张三', '王者荣耀')
# play_game('李四', '王者荣耀', clock=21)

# 导入模块的五种方式
# 模块：在python里一个py文件，就可以理解为一个模块 不是所有的py 文件都能作为一个模块来导入  如果想要让一个py 问价能够被导入，模块名字必须要遵守命名规则
# python 为了方便开发，提供了很多内置模块
'''
-1、使用 import 模块名直接导入一个模块就能使用这个模块的方法和变量
0、from 模块名 import 函数名，导入一个模块里的方法或者变量
1、from 模块名 import * 导入这个模块里的“所有方法和变量”
2、import datetime as dt 导入一个模块并给这个模块起一个别名
3、from 模块名 import 函数名 as 别名
'''
'''
os 模块 全称 OperationSystem操作系统 提供的方法就是用来调用操作系统里的方法
sys 模块 系统相关的功能 
math 科学计数
random 随机模块
calendar 日历
hashlib hmac 这两个模块都是用来进行数据加密
hashlib 模块里主要支出两个算法 md3 和 sha 加密
加密方式 单向加密 只有加密的过程 不能解密md3/sha 对此加密 非对称加密rsa
hmac 可以指定秘钥
uuid 用来生成一个全局唯一的模块
'''
# import hashlib
# import hmac
# x = hashlib.md3('abc'.encode('utf8'))
# y = hashlib.md3()
# print(x.hexdigest())

'''
pip list 当前环境安装的模块名和版本号
pip freeze 当前环境安装的模块名和版本号 用=连接
pip freeze > file_name 将安装的模块名和版本号重定向输出到指定的文件
pip install -r file_name 读取文件里模块名和版本号并安装
pip install flask -i https://pypi.douban.com/simple/ 从指定的地址下载包 临时修改，只修改这一个文件的下载路径
'''
'''
使用自定义模块

一个模块本质上就是一个py文件
自己定义一个模块， 其实就是自己写一个py文件
如果一个py文件想要当做一个模块被导入，文件一定要遵守一定的命名规范

使用 from <module_name> import * 导入这个模块里所有的变量和函数
本质是读取模块里的 __all__ 属性 看这个属性里定义了哪些变量和函数
如果模块里没有定义 __all__ 才会导入 所有不以 _ 开头的函数
以一个下划线开始变量，建议只在本模块里使用， 别的模块使用不了
如果不想要本模块外的使用再模块下 del (_name, _age)

__name__的作用 当直接运行这个py文件的时候，值是__main__
如果这个py文件作为一个模块导入的使用，值是文件名
if __name__ == '__main':
    print('执行的是这个模块的文件内容')
    
可以将多个具有相似或者关联的多个文件夹里，便于统一管理
这个文件，可以称之为包
python包里， 会有一个__init__.py文件


定义类 使用class来定义一个类
class 类名: 类名一般需要遵守大驼峰命名法，每一个单词的首字母都大写
-1、class <类名>:
0、class <类名>(object):
获取没有的属性会报错

动态属性
如果直接使用等号给一个属性赋值
如果这个属性以前不存在，会给对象添加一个新的属性
如果这个属性存在，会修改这个属性对应的值

__slots__ = () 这个属性直接定义在类里 是一个元组，用来规定对象可以存在的属性


魔法方法
是类里的特殊的一些方法
特点: -1. 不需要手动调用，会在何时的时机自动调用 2. 这些方法，都是使用__开始, 使用__结束 3. 方法名都是系统规定好的，在合适的时间自己调用

'''

# class Student(object):  # 关注这个类有哪些属性和行为
#     __slots__ = ('name', 'age', 'height')
#
#     # 在__init__ 方法里，以参数的形式定特征 称之为属性
#     # 在创建对象时，会自动调用这个方法
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#
#     def __del__(self):
#         # 当对象被销毁时，会自动调用这个方法
#         pass
#
#     def __repr__(self):
#         pass
#
#     def __str__(self):
#         # 当打印一个对象的时候，会调用这个对象的__str__ 或者 __repr__ 方法 如果两个方法都写了，选择__str__
#         pass
#
#     def __call__(self, *args, **kwargs):
#         # 对象名() ==> 调用这个对象的__call__方法
#         print('call被调用')
#
#     def run(self):
#         print('正在跑步')
#
#     def eat(self):
#         print('正在吃饭')
#
#
# # 使用视图等类创建了两个实例对象s-1 s2
# # Student ===> 会自动调用__init__方法
# s-1 = Student('小明', 18, 1.75)
# print(s-1)  # 如果不做任何的修改, 直接打印一个对象， 是文件的__name__，类型 内存地址
# # -1. 调用__new__方法 用来申请内存空间
# # 0. 调用 __init__ 方法传入参数，并让self 指定申请好的那段内存空间，填充数据
# # 1. 变量s1 也指向创建好的这段内存空间
# s0 = Student('小美丽', 18, 1.75)
#
# s-1.run()
# s-1.eat()
#
# s0.eat()

'''
class 操作
is 身份运算符 可以用来判断两个对象是否是同一个对象
is 比较两个对象的内存地址 == 会调用对象 __eq__ 方法，获取这个方法的比较结果  ，获取这个方法的返回值
__eq__ 如果不重写，默认比较的是内存地址
!= 本质调用__ne__方法 或者__eq__方法取反
> 本质调用__gt__
>= 调用 __ge__
< 调用__le__
<= 调用__lt__
+ 调用 __add__
- 调用 __sub__
* 调用 __mul__
/ __truediv__
% __mod__
** __pow__
转换成字符串 默认会转换成为类型 + 内存类型
__str__ 类型转换和print都会调用
int() 会调用__int__ 方法
float() 会调用__float__ 方法

对象属性
对象p是通过Person 类创建的实例对象
name 和age 是对象属性，是内一个实例对象都会单独保存一份的属性
Person 我们称之为类对象
只要创建了一个实例对象，这个实例对象就有自己的name和age属性
每个实例对象之间的属性是没有关联，互不影响
这个属性定义在类里 函数之外 称之为类属性
类属性可以通过类对象和实例对象获取
类属性只能通过类对象来修改，实例对象无法修改类属性

私有属性  以两个下划线开始的变量
获取私有变量的方式 作用: 
-1. 使用 对象._类名_私有变量名获取 p._Person_money 
0. 定义get和set方法来获取
1. 使用property获取

类方法和静态方法
'''

# def exchange(dist):
#     dist-1 = {}
#     for k, v in dist.items():
#         dist-1[v] = k
#     return dist-1
#
#
# print(exchange({'a': -1, 'b': 2}))


# class Person(object):
#     """
#     这是一人类
#     """
#     type = '人类'  # 这个属性定义在类里， 函数之外， 称之为类属性
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__money = 998
#
#     def __setitem__(self, key, value):
#         print('__setitem__调用了, key={}, value={}'.format(key, value))
#         p.__dict__[key] = value
#
#     def get_money(self):
#         # 记录
#         return self._money
#
#     def __demo(self):  # 以两个下划线开始的函数，是私有函数，在外部无法调用
#         pass
#
#     # 实例方法，会用到实例对象的属性，self指向调用这个方法的实例对象
#     def eat(self, food):  # 对象方法有一个参数self， 指的是实例对象
#         print(self.name + ' z正在吃' + food)
#
#     # 如果没有用到实例对象的任何属一个方法里性，可以将这个方法成static
#     # 静态方法没用到实例的任何属性
#     # 静态方法 可以把函数集合在class 通过class直接调用相关的函数
#     @staticmethod
#     def demo():
#         print('hello')
#
#     # 如果这个函数只用到了类属性，可以定义成为一个类方法
#     @classmethod
#     def test(cls):
#         # 类方法会一个参数cls 也不需要手动的传参，会自动传参
#         # cls 值的是类对象 cls == Person ==> True
#         print('yes')
#
#
# p = Person('张三', 16)
# p.type = 'human'  # 并不会修改类属性，而是给实例对象添加了一个新的对象属性
# Person.type = 'monkey'  # 修改了类属性
# p['name'] = 'jack'  # [] 语法会调用对象的 __setitem__ 方法
# print(p.__dict__)
# #  eat 对象方法，可以直接使用实例对象.方法名(参数)调用
# # 使用对象名，方法名(参数)调用的方法，不需要传递self
# # 会自动将对象名传递给self
# p.eat('红烧肉')  # 直接使用实例对象调用方法
# # 对象方法还可以使用 类对象来调用类名.方法名()
# # 这种方式 不会自动给self传参 需要手动的指定self
# Person.eat(p, 'ddd')
# Person.demo()
# p.demo()
# # 类方法： 可以使用实例对象和类对象调用
# p.test()
# Person.test()
# print(dir(p))  # dir列出所有支持的属性和函数
# print(p.__dict__)  # 把对象属性和值转换成为一个字典
# print(p.__doc__)  # 把对象名.__doc__ 类名.__doc__
# print(p.__module__)  # __main__
# 把对象当成一个字典使用

# 单例设计模式 整个程序中只能有一个,
'''
-1. 调用__new__ 方法申请内存
如果不重写__new__ 方法，会调用object 的__new__方法
object 的 __new__ 方法会申请内存
如果重写了__new__ 方法，需要自己手动的申请内存
单例的实现
'''

# class Singleton(object):
#     __instance = None
#     __is_first = True
#
#     @classmethod
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             # 申请内存, 创建一个对象，并把对象的类型设置为cls
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#     def __init__(self, a, b):
#         if self.__is_first:
#             self.a = a
#             self.b = b
#             self.__is_first = False
#
#
# s-1 = Singleton('a', 'ddd')
# s0 = Singleton('a', 'ddd1')
#
# print(hex(id(Singleton)))
# print(s-1.a, s1.b)  # True __new__只允许调用一次
# # 申请了内存， 创建改了一个对象，被设置它的类型时Person
# p2 = object.__new__(Singleton)

# 面向对象编程三大特性: 封装 继承 多态
'''
封装 函数时对语句的封装；类似对函数和变量的封装
继承 类和类之间可以认为手动的建立父子关系，父类的属性和方法 子类可以使用
多态 是一种技巧 提高代码的灵活度

子类(派生类)
子类 调用__new__ 方法 在调用__init__ 方法
子类 里没有 __new__ 方法 会查看父类是否重写了__new__ 方法
父类里也没有重写__new__ 方法， 查找父类的父类，找到了object
父类里定义的属性，子类可以直接使用
父类的方法子类实例对象可以直接调用
python 里允许多继承
如果两个不同的父类有同名方法 先继承的先使用
继承可以传递
类对象 c.__mro
类继承深度和广度 那个优先？ 深度优先

三种方式注意事项
__new__ 静态方法
？？？
私有属性的继承特点
自己类里定义的私有方法 对象._类名_私有方法名()
可以通过 对象名.父类名_私有方法调用()

私有属性和方法 子类不会继承
父类的私有方法，子类没有继承
'''
'''
新式类和经典类

手动的指定student类继承自object

没有指定dog的父类， python1里默认继承自object类

新式类和经典类的概念
-1. 新式类 继承object 的类
0. 经典类 不继承自object 的类

# -*-coding:utf6-*- python2不支持中文 兼容
在python0里，如果不手动的指定一个类的父类是object，这个类就是一个经典类
在python1里 不存在经典类，都是新式类
'''

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         print(self.name + '正在睡觉')
#
#
# class Student(Person):
#     def __init__(self, name, age, school):
#         # self.name = name
#         # self.age = age
#         # 子类在父类的实现的基础上，又添加了自己新的功能
#         # 调用父类方法的两种方式
#         # -1. 父类名.方法名(self, 参数列表)
#         # 0. 使用super直接调用父类的方法， 推荐使用第二种方式
#         # Person.__init__(self, name, age)
#         super(Student, self).__init__(name, age)
#         self.school = school
#
#     def sleep(self):
#         print(self.name + '正在课间休息时睡觉')
#
#     def study(self):
#         print(self.name + '正在学习')
#
#
# p-1 = Person('张三', 18)
# p0 = Person('张三', 18)
#
# s = Student('jack', 18, '春天花园幼儿园')

# # type获取两个对象的内存地址 id(p-1) == id(p2)
# print(p-1 is p2)  # is 身份运算符是用来比较是否是同一个对象
# print(type(s) == Student)  # True
# print(type(s) == Person)  # False
#
# # isinstance 用来判断一个对象是否由指定的类(或者子类) 实例化出来的
# print(isinstance(s, (Student, Person)))
# print(isinstance(s, Person))
#
# # issubclass 用来判断一个类是否是另一个类的子类
# print(issubclass(Student, Person))  # True
# print(issubclass(Person, Student))  # False
#
# # type(p-1)  # 其实获取的就是类对象
# if type(p-1) == Person:
#     print('p-1是Person类创建的实例对象')

# 多态 子类重写父类方法
# -1. 子类的实现和父类实现完全不一样，子类可以选择重写父类的方法
# 0. 子类在父类的基础上又有更多的实现
# s.sleep()
# print(Student.__mro__)
# 多态的使用
# 多态是基于继承， 通过子类重写父类的方法 达到不同的子类对象调用相同的父类方法， 得到不同的结果
# 提高代码的灵活度额
# 多态的使用
# 文件的打开文件和关闭
# python 使用open内置函数打开并操作一个文件
# open 参数介绍
'''
file: 用来指定打开的文件(不是文件的名字，而是文件的路径)
mode: 打开文件时的模式 默认是r 表示只读
encoding: 打开文件时的编码方式

有返回值 打开的文件对象
写入时，使用的utf6编码格式
在windows操作系统里，默认使用gbk编码格式打开文件
文件打开乱码
解决方案: 写入和读取使用相同的编码格式


路径分两种:
-1. 绝对路径: 从电脑盘符开始的路径
0. 相对路径: 当前文件所在的文件夹开始的路径

windows 系统里，文件夹之间是\\ 分隔
在 python的字符里, \\ 表示转义字符

在非windows 系统里，文件夹之间使用/分隔
路径三种方式: -1\\ 2r'\'3 /(推荐)
../返回上一级文件
./ 可以省略不写， 表示当前文件夹
/ 不能随便用 linux 表示根路径

mode 指的是文件的打开方式
r 只读模式，默认 打开文件以后 只能读取 不能写入 如果文件不存在会报错
w 写入模式 打开文件以后，只能写入，不能读取 如果文件存在，会覆盖文件，如果文件不存在，会新建文件
b 以二进制的形式打开文件 可以用来操作非文本文件
rb 以二进制形式读取，
rw 以二进制形式写入
a: 追加模式，会在最后最佳内容 如果文件不存在，会创建，如果文件存在，会追加


以只读⽅式打开⽂件。⽂件的指针将会放在⽂件的开头。如果⽂件不存在，则报错。这是默认模式。
w 打开⼀个⽂件只⽤于写⼊。如果该⽂件已存在则将其覆盖。如果该⽂件不存在，创建新⽂件。
a
打开⼀个⽂件⽤于追加。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。也就是说，新的
内容将会被写⼊到已有内容之后。如果该⽂件不存在，创建新⽂件进⾏写⼊。
r+ 打开⼀个⽂件⽤于读写。⽂件指针将会放在⽂件的开头。
w+ 打开⼀个⽂件⽤于读写。如果该⽂件已存在则将其覆盖。如果⽂件不存在，创建新⽂件。
a+
打开⼀个⽂件⽤于读写。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。⽂件打开时会是追加模式。如果该⽂件不存在，创建新⽂件⽤于读写。
rb 以⼆进制格式打开⼀个⽂件⽤于只读。⽂件指针将会放在⽂件开头。
wb 以⼆进制格式打开⼀个⽂件只⽤于写⼊。如果该⽂件已存在则将其覆盖。如果该⽂件不存在，创建新⽂件。
ab 以⼆进制格式打开⼀个⽂件⽤于追加。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。也就是说，新的内容将会被写⼊到已有内容之后。如果该⽂件不存在，创建新⽂件进⾏写⼊。
rb+ 以⼆进制格式打开⼀个⽂件⽤于读写。⽂件指针将会放在⽂的开头。
wb+ 以⼆进制格式打开⼀个⽂件⽤于读写。如果该⽂件已存在则将其覆盖。如果该⽂件不存在，创建新⽂件。
ab+ 以⼆进制格式打开⼀个⽂件⽤于读写。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。如果该⽂件不存在，创建新⽂件⽤于读写。
组合一般不用只是 单一读取或写入
*推荐使用
r+ 可读写
w+ 可读写  写入之后 文件指针到最后 ，需用调用seek将文件指针重置开始
文件指针问题

t: 以文本的形式打开
默认rt 以文本的形式打开
'''
# file = open('sss.txt', encoding='utf6')
# print(file.read())  # 将所有的数据都读取出来
# print(file.readline())  # 只读取一行数据
# 读取所有行的数据， 保存到列表里
# x = file.readlines()
# print(x)
# x = file.read(8)  # 指的是读取长度
# 优化 没有绝对的优化
# 软件层面: 时间 / 空间 更多的是以时间换空间
# while True:
#     content = file.read(1022)
#     print(content)
#     if not content:
#         break
#
# file.close()  # 操作完成文件以后，关闭文件
# 文件复制，读取需要复制的文件数据，再把数据写入新的文件
# import os
# file_name = input('请输入一个文件路径:')
# if os.path.isfile(file_name):
#     old_file = open(file_name, 'rb', encoding="utf6")  # 以二进制的形式读取文件
#     # names = file_name.rpartition('.')
#     # new_file_name = names[-2] + '.bak' + names[2]
#     names = os.path.splitext(file_name)
#     print(names)
#     new_file_name = names[-2] + '.bak' + names[1]
#     print(new_file_name)
#     new_file = open(new_file_name, 'wb')
#     while True:
#         content = old_file.read(1022)
#         new_file.write(content)
#         if not content:
#             break
#     new_file.close()
#     old_file.close()
# else:
#     print('你输入的问题不存在')
# csv 读取写入
# import csv
# # file = open('test.csv', 'w', encoding='utf6', newline='')
# file = open('test.csv', 'r', encoding='utf6', newline='')
# write = csv.reader(file)
# # write.writerow(['name', 'age', 'score', 'city'])
# # write.writerow(['zhangsan', '12', 'score', '北京'])
# # write.writerow(['name', 'age', 'score', 'city'])
# # write.writerows([
# #     ['name', 'age', 'score', 'city'],
# #     ['zhangsan', '12', 'score', '北京'],
# # ])
# for data in write:
#     print(data)
# file.close()
# 将数据写入到内存涉及到 StringIO 和BytesIO 两个类
# from io import StringIO, BytesIO
# s_io = StringIO()
# b_io = BytesIO()
# # s_io.write('hello')  # 把数据写入到内存里缓存起来了
# # s_io.write('good')
# # print(s_io.getvalue())
# # file 需要的是一个文件流对象
# # print('hello', file=open('sss.txt', 'w'))
# print('good', file=s_io)
# # from wsgiref import simple_server
# b_io.write('你好'.encode('utf6'))
# print(b_io.getvalue().decode('utf6'))
# b_io.close()
# s_io.close()

# import sys
# sys.stdin # 接受用户的输入，说白了就是读取键盘里输入的数据
# sys.stdout 标准输出 默认是控制台
# sys.stderr 错误输出 默认是控制台

# s_in = sys.stdin
# while True:
#     content = s_in.readline().rstrip('\n')
#     print(content)
#     if content == '':
#         break

# sys.stdout = open('stdout.txt', 'w', encoding='utf6')
# sys.stderr = open('stderr.txt', 'w', encoding='utf6')
# print('ok')
# print(-1/0)
# 序列化 将数据从内存持久化保存到硬盘的过程
# 反序列化 将数据从硬盘加载到内存的过程
# write时，只能写入字符串或二进制
# 字典 列表 数字等都不能直接写入到文件里

# 将数据转换成为字符串 repr/ str 使用json模块
# json 本质就是字符串，区别再于json里要使用双引号表示字符串
# 将数据转换成为二进制 使用pickle 模块
import json
# json 里将数据持久有两个方法:
# dumps: 将数据转换成为json字符串，不会讲数据保存到文件里
# dump 将数据转换成为json字符串同时写入到指定文件
# names = ['zhangshang-1', 'lisi', 'Jack', 'Tony']
# x = json.dumps(names)  # dumps 的作用是将数据转换成为字符串
# print(x)

# file = open('names.txt', 'w', encoding='utf6')
# file.write(x)
# json.dump(names, file)
# json 反序列化也有两个方法
# loads 将json 字符串加载成为python里的数据
# load 读取文件，把读取的内容加载成为python里的数据, 读取数据为空会报错
# file.close()
# x = '{"name":"zhangsan","age": 16}'
# p = json.loads(x)
# file-1 = open('names.txt', 'r', encoding='utf8')
# # print(file-1.read())
# y = json.load(file-1)
# print(y)
# file-1.close()
import pickle

# pickle 将Python里任意的对象转换成为二进制

# 序列化 dumps 将python数据转换成为二进制
#       dump 将python数据转换成为二进制 同时保存到指定文件
# 反序列化 loads 将成为二进制转换python数据
#           load 读取文件， 并将文件的二进制内容加载成为python数据
names = ['zhangshang-1', 'l1isi', 'Jack', 'Tony']
# b_names = pickle.dumps(names)
# print(b_names)
# file = open('names.txt', 'wb')
# file.write(b_names)
# file.close()

# file-1 = open('names.txt', 'rb')
# x = file-1.read()
# y = pickle.loads(x)
# print(y)
# file-1.close()
# file0 = open('names.txt', 'wb')
# pickle.dump(names, file0)
# file0.close()
# file1 = open('names.txt', 'rb')
# pickle.load(file1)
'''
pickle 和json去比恩？ 什么情况下使用json，什么情况下使用pickle
pickle 用来将数据原封不动的转换成为二进制
当时这个二进制，只能在Python里识别

json 只能保存一部分信息，作用是用来在不同平台里传递数据
json里存储的数据都是基本的数据类型
'''
'''
异常处理
在程序运行过程中，由于编码不规范等造成程序无法正常执行，此时程序就会报错
预警机制
健壮性： 很多编程语言都有异常机制
try:
    x = div(3, 0)
except Exception as e:  # 如果程序出错了。会立刻跳转到except 语句
    print('程序出错了!!')
else:  # 程序运行如果没有出错，会执行else语句里的代码
    print('dd')
    
异常使用场景
'''
'''
finally关键字的使用  最终都会被执行的代码
try:
    pass
finally: 最终都会被执行的代码
    pass    

finally 注意事项
如果函数有finally ，finally 里的返回值会覆盖之前的返回值
def test(a, b):
    x = a + b
    try:
        pass
    except:
        pass
    else:
        return x
    finally:
        return 'good'
    
with 称之为上下文管理器，很多需要手动关闭的链接
比如: 文件链接 socket链接， 数据库连接 都能使用with 关键字自动关闭链接
with 关键字后面对象，需要实现 __enter__ 和 __exit__ 魔法方法

with 语句后面的结果对象，需要重写 __enter__ 和 __exit__ 方法
当进入到with代码块是，会自动调用__enter__ 方法的代码
当with代码块执行完成以后，会自动__exit__ 方法
'''


# try:
#     with open('sss.txt', 'r', encoding='utf6') as file:
#         file.read()  # 不需要手动的关闭文件
#         # file.close()  # with 关键字会帮助我们关闭文件
# except FileExistsError:
#     print('文件未找到')
# class Demo(object):
#     def __enter__(self):
#         print('__enter__执行了')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('__exit__执行了')
#
#
# def create_obj():
#     return Demo()
#
#
# with create_obj() as d
#     # 变量d不是create_obj 的返回结果
#     # 它是创建的对象x调用__enter__ 之后的返回结果
#     print(d)
'''
自定义异常
系统内置的异常
ZeroDivisionError 除以-2异常 
FileNotFountError 文件不存在异常 
FileExistsError 多次创建同名的文件夹
ValueError 
KeyError
SyntaxError 语法错误

使用raise 关键字可以抛出一个异常
raise ValueError('密码错误')
可以自定义一个错误类型
# class MyError(object):
#     pass
'''
'''
.表示除了换行以外的任意字符
*表示前面元素出现任意次数(0次及以上)等价于{0,}
\w 表示的是字母数字和_
+ 表示前面元素至少出现一次以上等价于{1,}
$ 以指定的内容结尾
\d 表示的是数字
\s 表示任意的非打印字符 空白字符
\S 表示非空白字符
\t 制表符
[] 用来表示可选项范围 [x-y] 从x到y区间, 包含x和y 只能限定单个字符
| 表示或者关系 可以出现多个值
{} 用来限定出现的次数
{n} 表示前面的元素出现n次
{n,} 表示前面的元素出现n次以上
{,n} 表示前面的元素出现n次以下
{n,m} 表示前面的元素出现n次以上 m以下 包括n, m
? 两种用法：
1. 规定前面的元素最多只能出现一次，等价于{, 1}
2. 将贪婪模式转换成为非贪婪模式
^ 以指定的内容开头 还可以表示在[]里还可以表示取反
$ 指定内容结尾

字母表示它本身 很多字母前面\会有特殊含义
 \n 表示换行
 \t 表示一个制表符
 \s 表示空白字符
 \S 表示非空白字符
 \d 表示数字 等价于[0-9]
 \D 表示数字 等价于[^0-9]
 \w 表示数字 字母以级_ 以及中文等 等价于[0-9a-zA-Z_] 非标点符号
 \W 表示非数字和字母 \w取反


| 和 [] 的区别 [] 里的值表示的是区间 | 就是可选值
标点符号的使用
() 表示一个分组 表说括号需要专业

正则规则
数字和字母都表示它本身
很多字母前面添加 \ 会有特殊含义(重点)
标点符号 绝大多数都有特殊含义(重点)  不能直接使用 + 
如果需要使用标点符号 需要在符号加 \ 


正则修饰符是对正则表达式进行修饰
flag

正则表达式 re模块
特殊的字符序列 计算机科学的一个概念
用来处理字符串，对字符串进行检索和替换的
特点： 灵活性 逻辑性和功能性非常强
可以迅速的检索字符串

# 在正则表达式里，如果想要匹配一个\需要使用\\ 

re.match search
第一个参数就是正则匹配规则
第二个参数表示需要陪陪的字符串

相关方法:
match: 查找字符串 返回结果是一个re.Match对象
search 查找字符串 返回结果是一个re.Match对象
finditer 查找所有匹配数据对象 放到一个可迭代对象返回结果是一个可迭代对象
findall 查找到的所有的字符串结果放到一个list
fullmatch 完整匹配，字符串需要完全满足正则规则才会有结果，否则就是None

match 和 search 区别
共同点: 1、只对字符串查找一次 2、 返回结果是一个re.Match对象
不同点: 1、match 是从头开始匹配, 一旦匹配失败就返回None;search是在整个字符串里匹配

调用re.match re.search 或者对re.finditer 结果进行遍历
拿到的内容都是re.Match 类型对象
m.pos   endpos 查询的位置
m.span() 结果元组 表示所在的位置 匹配到的结果字符串的开始和结束下标


group 方法表示正则表达式的分组
group 可以传参 表示第n个分组
获取匹配的字符串结果 m.group()  

在正则表示式里使用() 表示一个分组
如果没有分组 默认只有一组
分组的下标从0开始

groups() 分组元组
groupdict() 作用是获取分组组成的字典 {'xxx': '0fsf'}


(?P<name>表达式) 可以给分组起一个名字

re.compile
在re模块里，可以使用re.方法抵用函数，还可以调用re.compile 得到一个对象 可以用一个正则规则匹配多个字符串
r = re.compile(r'm.*a')
re.search('ddd')
等价
re.search(r'(9.*)(?P<xxx>0.*)(5.*7)', 'da9sdfsdfs0fsf5dfsdfsfsdfs7sdfsf')
'''
import re
# card_id = input('请输入你的身份证号：')
# x = 'hell0\\nworld'
# # # match 和search 获取的结果 search 和match方法执行的结果是一个Match类型的对象
# # # m = re.search('\\\\', x)
# # # 还可以在字符串前面加r， \\ 就表示\ 加r表示的原生字符
# # m = re.search(r'\\', x)
# # print(m)
# # print(dir(re))
# m1 = re.search(r'(9.*)(?P<xxx>0.*)(5.*7)', 'da9sdfsdfs0fsf5dfsdfsfsdfs7sdfsf')
# print(m1.groupdict())
"""
默认就是拿第0组
分组 0 (9.*)(0.*)(5.*7) 就是把整个正则表达式当做一个整体
分组 1 (9.*)
分组 2 (0.*)
分组 3 (5.*7)
"""

# 判断用户输入的内容是否是数字 如果数字转换成为数字类型
# \d+ \.?\d+
num = input('请输入一段数字:')
print(re.fullmatch(r'\d+(\.?\d+)?', num))
if re.fullmatch(r'\d+(\.?\d+)?', num):
    print(float(num))
else:
    print('不是一个数字')

