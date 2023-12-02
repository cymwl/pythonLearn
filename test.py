# print("hello,world!")
# test1 = "chenchen"
# test2 = "chenchen2"
# year = 2023
# price = 123
# print("xxx%s,%sxxxx" % (test1, test2))
# print(f"我是{test1},我是{test2},现在是{year}年,价格是{price}")
# print("字符串在python中的类型是：%s" % (type("字符串")))
# name = input("告诉我你是谁")
# print(f"你是{name}")

# print("欢迎。。。。")
# age = int(input("输入年龄"))
# level=int(input("输入你的等级"))
# day=int(input("今天几号"))
# if age <= 18:
#     print("未成年免费")
# elif level>=2:
#     print("vip免费")
# elif day==1:
#     print("一号免费")
# else:
#     print("给钱")
# print("欢迎游玩")


# num=5
# your_num=int(input("请输入你猜的数字"))
# if your_num==num:
#     print("你猜对了")
# else:
#     your_num=int(input("不对，再猜一次"))
#     if your_num == num:
#         print("你猜对了")
#     else:
#         your_num = int(input("不对，再猜最后一次"))
#         if your_num == num:
#             print("你猜对了")
#         else:
#             print("全部错了，数字是%d"%(num))

# num=5
# your_num=int(input("请输入你猜的数字"))
# if your_num==num:
#     print("你猜对了")
# elif int(input("猜错了，再猜一次"))==num:
#     print("你猜对了")
# elif int(input("猜错了，再猜一次"))==num:
#     print("你猜对了")
# else:
#     print("全部错了，数字是%d" % (num))


'''
随机数猜测三次机会
'''
# import random
# num = random.randint(1, 10)
# num1 = int(input("请输入你猜的数字"))
# if num1 == num:
#     print("你猜对了")
# elif num1>num:
#     num1=int(input("你猜的大了,重新猜"))
#     if num1 == num:
#         print("你猜对了")
#     elif num1 > num:
#         num1 = int(input("你猜的大了,重新猜"))
#         if num1 == num:
#             print("你猜对了")
#         else:
#             num1 = int(input("错了没机会了"))
#     else:
#         num1 = int(input("你猜的小了,重新猜"))
#         if num1 == num:
#             print("你猜对了")
#         else:
#             num1 = int(input("错了没机会了"))
# else:
#     num1 = int(input("你猜的小了,重新猜"))
#     if num1 == num:
#         print("你猜对了")
#     elif num1 > num:
#         num1 = int(input("你猜的大了,重新猜"))
#         if num1 == num:
#             print("你猜对了")
#         else:
#             num1 = int(input("错了没机会了"))
#     else:
#         num1 = int(input("你猜的小了,重新猜"))
#         if num1 == num:
#             print("你猜对了")
#         else:
#             num1 = int(input("错了没机会了"))


# i=1
# x=0
# while i<=100:
#     x+=i
#     i+=1
# print(x)


# import random
# num=random.randint(1,100)
# you_num=int(input("你猜的数字"))
# i=1
# while you_num!=num:
#     if you_num>num:
#         print("big")
#     else:
#         print("small")
#     you_num=int(input("重新猜"))
#     i+=1
# else:
#     print(f"你在第{i}次猜对了")


# print("hello\tworld")
# print("gg\t\tbeng")


'''
99乘法表
'''
# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print(f"{j}*{i}={j*i}\t",end=" ")
#         j+=1
#     i+=1
#     print("")


# i=0
# name="aaachenaachenaachenaaa"
# for x in name:
#     print(x,end="")
#     if x=="a":
#         i+=1
# print(f"中一共有{i}个a")


'''
输入数字并且计算出偶数个数
'''
# i=int(input("请输入数字"))
# count=0
# for x in range(1,i+1):
#     print(f"{x}\t",end="")
#     if x%2==0:
#         count+=1
# print()
# print(f"0到{i}一共有{count}个偶数")


'''
极简99乘法表
'''
# for i in range(10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j*i}\t",end=" ")
#     print("")


'''
发工资案列
'''
# salary = 10000
# while salary!=0:
#     for x in range(1, 21):
#         num = random.randint(1, 10)
#         if num >= 5:
#             salary -= 1000
#             print(f"员工{x},绩效分{num},发工资，剩下{salary}")
#         else:
#             print(f"员工{x},绩效分{num},不发工资，下一位")
#         if salary!=0:
#             continue
#         else:
#             break


'''
函数学习
'''

# def cheak(int):
#     if int<=37.5:
#         print("yes")
#     else:
#         print("no")
#
# wendu=int(input("insert your tiwen"))
# cheak(wendu)
#
#
# def add(a,b):
#     c=a+b
#     return c
# x=add(9,9)
# print(x)


# def add(a,b):
#     '''
#
#     :param a: 加数
#     :param b: 加数
#     :return: 和
#     '''
#     c=a+b
#     return c
#
# x=add(3 ,6)
# print(x)


# money=5000000
# def select():
#     print(money)
# def add(x):
#     global money
#     money+=x
#     print(f"存成功,余额{money}")
# def qu(x):
#     global money
#     money-=x
#     print(f"取成功,余额{money}")
# def methd():
#     q = int(input("你好，请选择操作.\n查询余额\t输入1\n存款\t\t输入2\n取款\t\t输入3\n退出\t\t输入4\n"))
#     if q==1:
#         select()
#     elif q==2:
#         add(int(input("存多少钱")))
#     elif q==3:
#         qu(int(input("取多少")))
#     else:
#         print("退出成功")
# y=int(input("需要服务输入1，退出按2\n"))
# while y==1:
#     methd()
#     y=int(input("如果还需要服务请输入1\n不需要请输入2\n"))
# else:
#     print("退出")


# list_student=[21,25,21,31,23,22,20]
# list_student.append(25)
# print(list_student)
# list2=[15,55,66]
# list_student.extend(list2)
# print(list_student)
# last_one=list_student.pop(-1)
# print(last_one)
# print(list_student)
# first_one=list_student.pop(0)
# print(first_one)
# print(list_student)
# index_31=list_student.index(31)
# print(index_31)
# for i in range(0,len(list_student)):
#     print(list_student[i]," ",end="")


# list_1=[1,2,3,4,5,6,7,8,9,10]
# list_2=[]
# def select():
#     for i in list_1:
#         if i%2==0:
#             list_2.append(i)
# select()
# print(list_2)


# z1=('周杰伦',11,['football','music'])
# print(z1.index(11))
# print(f"name=:{z1[0]}")
# z1[2].remove('football')
# z1[2].append('coding')
# print(z1)


# str1='itheima itcast boxuegu'
# i=str1.count('it')
# print(i)
# str2=str1.replace(' ','|')
# print(str2)
# str3=str1.split('|')
# print(str3)


# my_set=set()
# my_list=['asdasd','dwa','w','we','dqwd','dwa','dwa']
# for e in my_list:
#     print(e)
#     my_set.add(e)
# print(f"myset element:{my_set}\nzqde my list:{my_list}")
#


# my_dict = {
#     "wlh": {
#         "work": "kj",
#         "salary": 3000,
#         "level": 1
#     },
#     "zjl": {
#         "work": "sc",
#         "salary": 5000,
#         "level": 2
#     },
#     "ljj": {
#         "work": "sc",
#         "salary": 7000,
#         "level": 3
#     },
#     "zxy": {
#         "work": "kj",
#         "salary": 4000,
#         "level": 1
#     },
#     "ldh": {
#         "work": "sc",
#         "salary": 4000,
#         "level": 2
#     },
# }
# for key in my_dict:
#     if my_dict[key]["level"] == 1:
#         emplyee_info_dict = my_dict[key]
#         emplyee_info_dict["level"] = 2
#         emplyee_info_dict["salary"] += 1000
#         my_dict[key] = emplyee_info_dict
# print(my_dict)


# def dy(name,age,gender):
#     print(name,age,gender)
# dy("cc",1,"man")
# dy(age=8,name="ccc",gender="woman")
# dy("ww",gender="man",age=89)


# def test_func(xxx):
#     result = xxx(1, 2)
#     print(result)
#
#
# def yyy(x, y):
#     return x + y
#
#
# test_func(yyy)


"""
函数多返回值 代码示例
"""

# 定义函数 : 加法
# def add(x, y):
#     return x + y
#
#
# # 定义函数 : 减法
# def minus(x, y):
#     return x - y
#
#
# # 定义函数 : 乘法
# def multiple(x, y):
#     return x * y
#
#
# # # 定义函数 : 除法
# def division(x, y):
#     return x / y
#
#
# # 函数中接收另外一个函数作为函数
# def caculate_num(action):
#     result = action(4, 2)
#     print(result)
#
#
# # 将 add 函数作为参数 传递给 caculate_num 函数
# caculate_num(add)  # 6
#
# caculate_num(minus)  # 2
#
# caculate_num(multiple)  # 8
#
# caculate_num(division)  # 2.0
#
# caculate_num(lambda x,y:x%y)


# f=open("D:/pythonDemo/测试.txt","r",encoding="UTF-8")
# print(type(f))
# lb=f.read()
# print(lb)
# f.close()


#
# with open("D:/pythonDemo/test.txt","r",encoding="UTF-8") as f:
#     my_list=f.read()
#     print(my_list.count("itheima"))


# with open("D:/pythonDemo/testWrite.txt","a",encoding="UTF-8") as f:
#     f.write("abcabc chenchen")
#     f.flush()


# def func_1():
#     print("func_1 action")
#     1/0
#     print("func_1 end")
# def func_2():
#     print("func_2 action")
#     func_1()
# if __name__ == '__main__':
#     try:
#         func_2()
#     except Exception as e:
#         print(f"出现异常，异常信息为：{e}")

# import my_module01
# i=my_module01.add_1(4,5)
# print(i)


# import my_package.my_module01
# import my_package.my_module02
# my_package.my_module01.func_module01()
# my_package.my_module02.func_module02()


"""
自定义包自定义模板方法使用案列
"""
# list_1="asdasfasfasfa"
# list_2="xxxxaaayyxaaxyyyxaxayyyxayyaaxxxxayy"
# import my_untils.str_util
# import my_untils.file_util
#
# mylist=my_untils.str_util.str_reverse(list_1)
# print(mylist)
#
# mylist2=my_untils.str_util.substr(list_2,2,4)
# print(mylist2)
#
# try:
#     my_untils.file_util.print_file_info("D:/pythonDemo/testWrite.txt")
# except Exception as e:
#     print("文件不存在")
#
# my_untils.file_util.append_to_file("D:/pythonDemo/testWrite.txt","add massage")


"""
图标学习，折线图
"""

# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, LegendOpts, TooltipOpts, VisualMapOpts
#
# line=Line()
# line.add_xaxis(["cc","ww","cw"])
# line.add_yaxis("test",[50,95,65])
# line.set_global_opts(
#     #配置标题
#     title_opts=TitleOpts(title="测试",pos_left="center",pos_bottom="1%"),
#     #鼠标移动效果
#     legend_opts=LegendOpts(is_show=True),
#     #工具箱
#     toolbox_opts=TooltipOpts(is_show=True),
#     #视觉映射
#     visualmap_opts=VisualMapOpts(is_show=True),
# )
#
# line.render()


"""
疫情折线图学习代码
"""
# from pyecharts.charts import Line

# f_us = open("D:\pythonDemo\美国.txt", "r", encoding="UTF-8")
# from pyecharts.charts import Line
#
# f_jp = open("D:\pythonDemo\日本.txt", "r", encoding="UTF-8")
# from pyecharts.charts import Line
#
# f_in = open("D:\pythonDemo\印度.txt", "r", encoding="UTF-8")
#
# # us
# us_data = f_us.read()
# us_data = us_data.replace("jsonp_1629344292311_69436(", "")
# us_data = us_data[:-2]
# us_dict = json.loads(us_data)
# us_trend_data = us_dict['data'][0]['trend']
# us_x_data = us_trend_data['updateDate'][:314]
# us_y_data = us_trend_data['list'][0]["data"][:314]
#
# # jp
# jp_data = f_jp.read()
# jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
# jp_data = jp_data[:-2]
# jp_dict = json.loads(jp_data)
# jp_trend_data = jp_dict['data'][0]['trend']
# jp_x_data = jp_trend_data['updateDate'][:314]
# jp_y_data = jp_trend_data['list'][0]["data"][:314]
#
# # in
# in_data = f_in.read()
# in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# in_data = in_data[:-2]
# in_dict = json.loads(in_data)
# in_trend_data = in_dict['data'][0]['trend']
# in_x_data = in_trend_data['updateDate'][:314]
# in_y_data = in_trend_data['list'][0]["data"][:314]
#
# line = Line()
# line.add_xaxis(us_x_data)
# line.add_yaxis('米国', us_y_data, color="blue", label_opts=LabelOpts(is_show=False))
# line.add_yaxis('日本', jp_y_data, color="red", label_opts=LabelOpts(is_show=False))
# line.add_yaxis('印度', in_y_data, color="black", label_opts=LabelOpts(is_show=False))
# # 配置图表全局设置
# line.set_global_opts(
#     # 配置标题
#     title_opts=TitleOpts(title="2020年疫情确诊图", pos_left="center", pos_bottom="1%"),
#     # 鼠标移动效果
#     legend_opts=LegendOpts(is_show=True),
#     # 工具箱
#     toolbox_opts=TooltipOpts(is_show=True),
#     # 视觉映射
#     visualmap_opts=VisualMapOpts(is_show=True),
# )
# line.render()


"""
地图学习代码
"""
# from pyecharts.charts import Map
# map=Map()
#
# data=[
#     ("北京市",9),
#     ("上海市",19),
#     ("湖南省",299),
#     ("台湾省",3999),
#     ("广东省",49999)
# ]
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         #设置颜色柱体
#         pieces=[
#             {"min":1,"max":9,"label":"1-9人","color":"#CCFFFF"},
#             {"min":10,"max":99,"label":"10-99人","color":"#FFFF99"},
#             {"min":100,"max":499,"label":"99-4999人","color":"#FF9966"},
#             {"min":500,"max":999,"label":"499-999人","color":"#FF6666"},
#             {"min":1000,"max":9999,"label":"1000-9999人","color":"#CC3333"},
#             {"min":10000,"label":"10000以上","color":"#990033"}
#         ]
#     )
# )
# map.add("地图测试",data,"china")
# map.render()


"""
河南省疫情确诊地图
"""
# from pyecharts.charts import Map
# f=open("D:\pythonDemo\疫情.txt","r",encoding="UTF-8")
# total_data=f.read()
# f.close()
# #获得省份列表
# total_data=json.loads(total_data)
# province_data_list=total_data["areaTree"][0]["children"]
# #获得个省份名称和确证人数
# data_list=[]
# for province_data in province_data_list:
#     province_name=province_data["name"]+"省"
#     province_confirm=province_data["total"]["confirm"]
#     data_list.append((province_name, province_confirm))
#
# print(data_list)
# map=Map()
# map.add("疫情测试地图",data_list,"china")
# #地图全局设置
# map.set_global_opts(
#     title_opts=TitleOpts("全国疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         #设置颜色柱体
#         pieces=[
#             {"min":1,"max":99,"label":"1-9人","color":"#CCFFFF"},
#             {"min":100,"max":999,"label":"10-99人","color":"#FFFF99"},
#             {"min":1000,"max":4999,"label":"99-4999人","color":"#FF9966"},
#             {"min":5000,"max":9999,"label":"499-999人","color":"#FF6666"},
#             {"min":10000,"max":99999,"label":"1000-9999人","color":"#CC3333"},
#             {"min":100000,"label":"10000以上","color":"#990033"}
#         ]
#     )
# )
# map.render("全国疫情地图.html")
#
#
# f=open("D:\pythonDemo\疫情.txt","r",encoding="UTF-8")
# total_data=f.read()
# f.close()
# #获得省份列表
# total_data=json.loads(total_data)
# provinceHeNan_data_list=total_data["areaTree"][0]["children"][3]["children"]
# #print(provinceHeNan_data_list)
#
#
# Hn_data_list=[]
# for shiqu_data in provinceHeNan_data_list:
#     shiqu_name=shiqu_data["name"]+"市"
#     shiqu_confirm=shiqu_data["total"]["confirm"]
#     Hn_data_list.append((shiqu_name, shiqu_confirm))
#
# Hn_data_list.append(("济源市",5))
# print(Hn_data_list)
# map=Map()
# map.add("河南疫情测试地图",Hn_data_list,"河南")
# #地图全局设置
# map.set_global_opts(
#     title_opts=TitleOpts("河南疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         #设置颜色柱体
#         pieces=[
#             {"min":1,"max":99,"label":"1-9人","color":"#CCFFFF"},
#             {"min":100,"max":999,"label":"10-99人","color":"#FFFF99"},
#             {"min":1000,"max":4999,"label":"99-4999人","color":"#FF9966"},
#             {"min":5000,"max":9999,"label":"499-999人","color":"#FF6666"},
#             {"min":10000,"max":99999,"label":"1000-9999人","color":"#CC3333"},
#             {"min":100000,"label":"10000以上","color":"#990033"}
#         ]
#     )
# )
# map.render("河南省疫情地图.html")


"""
时间线测试
"""
# from pyecharts.charts import Bar, Timeline
#
# bar1=Bar()
# bar1.add_xaxis(["CN","US","UK"])
# bar1.add_yaxis("GDP",[50,40,60])
# bar1.reversal_axis()
# bar2=Bar()
# bar2.add_xaxis(["CN","US","UK"])
# bar2.add_yaxis("GDP",[90,60,20])
# bar2.reversal_axis()
# bar3=Bar()
# bar3.add_xaxis(["CN","US","UK"])
# bar3.add_yaxis("GDP",[80,40,100])
# bar3.reversal_axis()
#
# timeline=Timeline({"theme":ThemeType.LIGHT})
# timeline.add(bar1,"点1")
# timeline.add(bar2,"点2")
# timeline.add(bar3,"点3")
# #设置自动播放
# timeline.add_schema(
#     play_interval=1000,     #设置自动播放时间
#     is_timeline_show=True,  #是否显示时间线
#     is_auto_play=True,      #是否自动播放
#     is_loop_play=True       #是否循环播放
# )
# timeline.render("时间线测试.html")


"""
多组数据时间线测试
"""
#
# from pyecharts.charts import Bar
# from pyecharts.charts import Timeline
# from pyecharts.globals import ThemeType
# from pyecharts.options import LabelOpts, TitleOpts
#
# f=open("D:/pythonDemo/1960-2019全球GDP数据.csv","r",encoding="ANSI")
# total_lines=f.readlines()
# f.close()
# total_lines.pop(0)
#
# data_dict={}
# for line in total_lines:
#     year=int(line.split(",")[0])    #get year
#     country=line.split(",")[1]
#     GDP=float(line.split(",")[2])
#     try:
#         data_dict[year].append([country,GDP])
#     except KeyError:
#         data_dict[year]=[]
#         data_dict[year].append([country, GDP])
#
# timeline=Timeline({"theme":ThemeType.LIGHT})
# sorted_year_list=sorted(data_dict.keys())
# for year in sorted_year_list:
#     data_dict[year].sort(key=lambda element:element[1],reverse=True)
#     year_data=data_dict[year][0:8]
#     x_data=[]
#     y_data=[]
#     for country_gdp in year_data:
#         x_data.append(country_gdp[0])
#         y_data.append(country_gdp[1]/100000000)
#
#     bar=Bar()
#     x_data.reverse()
#     y_data.reverse()
#     bar.add_xaxis(x_data)
#     bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))
#     bar.reversal_axis()
#
#     bar.set_global_opts(
#         title_opts=TitleOpts(title=f"{year}年全球前八GDP数据")
#     )
#     timeline.add(bar,str(year))
#
# timeline.add_schema(
#     play_interval=1000,     #设置自动播放时间
#     is_timeline_show=True,  #是否显示时间线
#     is_auto_play=True,      #是否自动播放
#     is_loop_play=True       #是否循环播放
# )
# timeline.render("1960——2019GDP.html")


"""
对象学习
"""


# class student:
#     name=None
#     age=None
#     gender=None
#
#
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#
#     def __str__(self):
#         return f"name={self.name},age={self.age},gender={self.gender}"
#
#     def say(self):
#         print(f"age={self.age}")
#
#     def __lt__(self, other):
#         return self.age<other.age
#
#
# std1=student("cc",15,"man")
# std2=student("cy",19,"man")
# print(std1>std2)
# print(std1<std2)
# std1.say()
# print(std1)

"""
多态测试
"""
# class animal:
#     def speak(self):
#         pass
#
#
# class cat(animal):
#     def speak(self):
#         print("mmm")
#
#
# class dog(animal):
#     def speak(self):
#         print("www")
#
#
# def make_noise(animal: animal):
#     animal.speak()
# cat=cat()
# dog=dog()
#
#
# make_noise(cat)


'''
数据库连接代码
'''
# from pymysql import Connection
# conn=Connection(
#     host='localhost',
#     port=3306,
#     user='root',
#     password="145371",
#     autocommit=True
# )
# # print(conn.get_server_info())
# curor=conn.cursor()
# conn.select_db("t1")
# # curor.execute("create table test_pymysql(id int);")
# curor.execute("select * from user")
#
# results=curor.fetchall()
# print(results)
# curor.execute("insert into user values(10, '王王王王', 18, 1, '17628285006')")
# conn.close()


'''
spark学习
'''
from pyspark import SparkConf, SparkContext
#创建SparkConf类对象
conf=SparkConf().setMaster("local[*]").\
    setAppName("test_spark_app")
#基于sparkConf类对象创建SparkContext对象
sc=SparkContext(conf=conf)
#打印Spark的运行版本
print(sc.version)
#停止SparkContext对象的运行（停止Spark程序）
sc.stop()





























