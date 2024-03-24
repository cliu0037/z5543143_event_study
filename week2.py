# tic = QAN.AX

#  variable2 = """John said: "Let's learn Python together"."""
#  print(variable2)

# #
# # Using triple quotes
# str1 = '''John said, "Let's learn Python together".'''
#
# str2 = """John said, "Let's learn Python together"."""
#
# # Using backslash to escape the quotation mark
# str3 = "John said, \"Let's learn Python together\"."
#
# str4 = 'John said, "Let\'s learn Python together".'

# a = 1.
# print(a)
#
# 4/2

# i = 1
# test = i==1
# print(test)
#
# f = 0.2+0.2+0.2
# print(f)
# print(f==0.6)

# i=1.
# print(type(i))

# 'x'*3

# x = str('abc')
# xup = str.upper(x)
# print(xup)

# weird_case = "My fUnNy tYpEcAsE sTrInG"
# weird_case_lower = weird_case.lower()
# print(weird_case_lower)

# a = True
# b = 5
# print(f"The value of a is {a} and the value of b is {b}")

# a = True
# b = 5
# print("The value of a is {} and the value of b is {}".format(a , b))

# x = str(5)
# print(x)
# print(type(x))
#
# str = "very bad idea"
#
# x = str(5)
# print(x)
#
# del(x)
#
# x = str(5)
# print(x)

# length = 56
# width = 33
# height = 30.5
# volume = (length*width*height)
# print(f"the volume of this box is {volume} cubic centimeters")
#
# my_list = [ "First", "Second", "Third", "Fourth"]
# my_list[3]

# lst = [2, "string", True, None, True]
# print(f"Original lst is {lst}")
#
# lst.remove(True) ### take a look of the output, 1 will be removed.
# print(f"lst after removing the first True is {lst}")

# domain_name = "From firstname.surname@unsw.edu.au Mon Feb 19 10:10:15 2024".split('@')[1].split()[0]
# print(domain_name)

# username = input("請輸入使用者名稱:")
# if username.isalnum():
#     print("全部都是數字和英文字");
# else:
#     print("包含其他字元")

# str1 = '''This string cannot span
# more than one line'''

# str3 = """John said, \"Let's learn Python together\"."""
# print(str3)

# import math
# f = 0.2 + 0.2 + 0.2
# print(math.isclose(f, 0.6))

# x = str('abc')
# xup = str.upper(x)
# print(xup)

# y = 'abc'.upper()
# print(y)

# print("Hi".center(21,'-'))
#
# a = True
# b = 5
# print("The value of a is {} and the value of b is {}.".format(a, b))
# print(f"The value of a is {a} and the value of b is {b}.")

# lst = ["a", "b", "c", "d", "e", "f"]
# print(f"lst[:3] gives {lst[:3]}")
# print(f"lst[0:1000] gives {lst[0:1000]}")

# lst_a = [1] # lst_a is [1]
# lst_a.append(2) # lst_a is now [1, 2]
# print(lst_a)

# line = "welcome to the class"
# x = line.split()
# print(x)

# # Create a tuple with two elements
# tup = (1, 2)
# # unpack the tuple into two variables:
# (a, b) = tup
# # print
# print(f"`a` is {a} and `b` is {b}") # --> "a is 1 and b is 2"

# s = set()
# s.add("QAN.AX") # s is {"QAN.AX"}
# s.add("WES.AX") # s is {"QAN.AX", "WES.AX"}
# s.add("CBA.AX") # s is {"QAN.AX", "WES.AX", "CBA.AX"}
# s.add("CBA.AX") # s is {"QAN.AX", "WES.AX", "CBA.AX"} (so no change)
# print(f"After adding objects, s is {s}")
# s.remove("CBA.AX") # s is {"QAN.AX", "WES.AX"}
# print(f"After removing 'CBA.AX', s is {s}")
# print("QAN.AX" in s)

# prc_dic = {
#  '2020-01-02': 7.1600,
#  '2020-01-03': 7.1900,
#  '2020-01-06': 7.0000,
#  '2020-01-07': 7.1000,
#  '2020-01-08': 6.8600,
#  '2020-01-09': 6.9500,
#  '2020-01-10': 7.0000,
#  }
# prc_dic['2020-01-07'] = 6.9200
# print(prc_dic)
# print(prc_dic['2020-01-10'])

# d = {'a': 1, 'b': 2 }
# d.pop('a')
# print(f"After popping 'a', d is now {d}")

# w = "What"
# i = "IS"
# c = "CamelCase?"
#
# print('{} {} {}'.format(w, i.lower(),c))

# import yfinance
# tic = "QAN.AX"
# start = '2020-01-01'
# end = None
# # print(df.download("QAN.AX", '2020-01-01', None).to_csv('qan_stk_prc.csv'))

# # Downloads Qantas share price beginning 1 January 2020
# import yfinance

# df = yfinance.download(tic, start, end)
# print(df)
# print(df.to_csv('qan_stk_prc.csv'))

# a = 'this is called'
# b = 'problem'
# a = f'{a} Parsons {b}'
# b = print
# b(a)
#
# t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
# print(t[:-5])

# After Python 3.6, order of insertion is preserved
# dic = {1: 'first', 2: 'second', 3: 'third'}
# # This will insert the 0 key at the end
# dic[0] = 'fourth'
# #print(dic)
# # This will NOT insert the key at the end because 1 exists
# dic[1] = 'new first'
# #print(dic)
# # Also, this does not return the first element of the dic
# # because it was inserted at the end
# dic[0]
# print(dic)
# dic0 = {'a': 1, 'b': 2, 'c': 3}
# dic1 = dic0.update({'a': 0, 'd': 4})
# print(dic0[0])

# dic = { ['a', 'b']: 1, 'c': 2,}
# dic = { ('a', 'b'): 1, 'c': 2, }
# tup = (1, 2, ['a', 'b'])
# dic = {tup: 'value'}
# tup = (1, 2, ('a', 'b'))
# dic = {tup: 'value'}
# print(dic)

# list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
# list_b = ['good', 'nice', 'friendly']
#
# sol = list_a[1:]
# sol.remove('bad')
# sol.remove('bad')
# sol.append('including')
# sol.insert(2,'good')
# print(sol)

# lst_a = ['a']
# lst_b = ['b', lst_a]
# lst_c = ['b', ['a']]
#
# print(lst_b[1])

# f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
# f_suburbs.remove("Randwick")
# f_suburbs.remove("Kensington")
# f_suburbs.add("Fairfield")
# f_suburbs.add("Fairfield East")
# f_suburbs.add("Fairfield Heights")
# f_suburbs.add("Fairfield West")
# f_suburbs.add("Fairlight")
# f_suburbs.add("Fiddletown")
# f_suburbs.add("Five Dock")
# f_suburbs.add("Flemington")
# f_suburbs.add("Forest Glen")
# f_suburbs.add("Forest Lodge")
# f_suburbs.add("Forestville")
# f_suburbs.add("Freemans Reach")
# f_suburbs.add("Frenchs Forest")
# f_suburbs.add("Freshwater")
# print(f_suburbs)

# Fibonacci_sequence = (0,1,1,2,3,5,8,13,21,34)
# current = 21
# last =13
# current,last=Fibonacci_sequence[-1],Fibonacci_sequence[-2]
# print(current)
# print(last)

f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop("Randwick")
f_suburbs.pop("Kensington")
f_suburbs["Fairfield"]=10000
f_suburbs["Fairfield East"]=5273
f_suburbs["Fairfield Heights"]=7517
f_suburbs["Fairfield West"]=11575
f_suburbs["Fairlight"]=5840
f_suburbs["Fiddletown"]=233
f_suburbs["Five Dock"]=9356
f_suburbs["Flemington"]=None
f_suburbs["Forest Glen"]=None
f_suburbs["Forest Lodge"]=4583
f_suburbs["Forestville"]=8329
f_suburbs["Freemans Reach"]=1973
f_suburbs["Frenchs Forest"]=13473
f_suburbs["Freshwater"]=8866

print(f_suburbs)

