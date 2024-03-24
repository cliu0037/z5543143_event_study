# def qan_tic():            # (1)
#     tic = "QAN.AX"        # (2)
#     print(tic)            # (3)
#     return tic            # (4)
# res = qan_tic()
# print(res)

# def qan_tic():            # (1)
#     tic = "QAN.AX"        # (2)
#     # return tic            # (4)     <-- Function will exit here!
#     print(tic)            # (3)     <-- Will not be printed!
#
# # Call the function
# res = qan_tic()           # (5b)
#
# print(res)

# def qan_tic():            # (1)
#     tic = "QAN.AX"        # (2)
#     print(tic)            # (3)
#     return tic            # (4)

# print(qan_tic)
# print(tic)

# def qan_tic():            # (1)
#     tic = "QAN.AX"        # (2)
#     print(tic)            # (3)
#     return tic            # (4)
#
# tic = "WES.AX"            # (5)
# print(tic)                # (6)
# qan_tic()                 # (7)

# def mk_csv_name(tic):                   # (1)
#     tic = tic.lower()                   # (2)
#     tic_base = tic.split('.')[0]        # (3)
#     return f'{tic_base}_stk_prc.csv'    # (4)
#
# name = mk_csv_name('QAN.AX')            # (5)
# print(name)                             # (6)

# def evennumbers(list, n=0):
#     # base case
#     if n == len(list):
#         exit()
#     if list[n] % 2 == 0:
#         print(list[n], end=" ")
#     # calling function recursively
#     evennumbers(list, n+1)
# # Initializing list
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
# print("Even numbers in the list:", end=" ")
# evennumbers(list1)

# def print_even_numbers(numlist):
#     even_numbers = [num for num in numlist if num % 2 == 0]
#     print(even_numbers)
#     return even_numbers
#
# # Test the function with the provided list
# number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
# print_even_numbers(number_list)

# lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
# def print_square_numbers(numlist):
#     square_numbers = [num**2 for num in numlist if num**2 >= 150]
#     print(square_numbers)
#     return square_numbers
# print_square_numbers(lst)
#
# square_greater_150 = [i**2 for i in lst if i**2 > 150]
# print(square_greater_150)

# numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
# divisible_by_two = list({i for i in numbers if i % 2 == 0})
# print(divisible_by_two)




# def process_string(s):
#     # Split the string into words using split() method
#     words = s.lower().split()
#     # Remove non-alphanumeric characters from each word
#     # words = [''.join(filter(str.isalnum, word)) for word in words]
#     # Remove empty strings from the list
#     # words = [word for word in words if word]
#     return words
#
#     # Test the function
# print(process_string("This is my test String!"))

# def process_string(s):
#     words = s.split()
#     processed_words = list()
#     for i, word in enumerate(words):
#         if i % 2 == 0:
#             processed_words.append(word.lower())
#         else:
#             processed_words.append(word.upper())
#     return processed_words
#
# # Test the function
# print(process_string("This is my test String"))

# def fizz_buzz_sumz(i):
#     sum = 0
#     for x in range(1, i + 1):
#         if x % 3 == 0 and x % 5 != 0:
#             sum += 3 * x
#         elif x % 5 == 0 and x % 3 != 0:
#             sum += 5 * x
#         elif x % 3 != 0 and x % 5 != 0:
#             sum += x
#     return sum
#
# # Test the function
# print(fizz_buzz_sumz(10))  # Output should be 151

# def my_function(x):
#     x = x + 1
#     return x
#
# x = 3
# my_function(x)
# print(x)

# def my_function(x):
#     x = x + 1
#     return x
#
# x = 3
# x = my_function(x)
# print(x)

# def my_function(y):
#     global x
#     y = y + x
#     x = 2
#     y = y + x
#     return y
#
# x = 3
# y = 10
# y = my_function(x)
# print(y)

# def get_and_print_five():
#     five = get_five()
#     print(f'Called get_five(): result is {five}')
# def get_five():
#     return 5
#
# get_and_print_five()

# prc_dic = {
#   '3000-01-15': 7.0400,
#   '2020-01-14': 7.1100,
#   '2020-01-13': 7.0200,
#   '2020-01-02': 7.1600,
#   '2020-01-03': 7.1900,
#   '2020-01-06': 7.0000,
#   '2020-01-07': 7.1000,
#   '2020-01-08': 6.8600,
#   '2020-01-09': 6.9500,
#   '2020-01-10': 7.0000,
# }
#
# # Task 1: Define a variable sorted_keys containing the keys of prc_dic in ascending order
# sorted_keys = [key for key in sorted(prc_dic.keys())]
#
# # Task 2: Replace the prc_dic key for '3000-01-15' with '2020-01-15'
# prc_dic['2020-01-15'] = prc_dic.pop('3000-01-15')
#
# print(sorted_keys)
# print(prc_dic)

# def find_even_numbers(input_list):
#     even_numbers = [num for num in input_list if num % 2 == 0]
#     print(even_numbers)
#     return even_numbers
#
# # Test case
# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
# result = find_even_numbers(input_list)
# find_even_numbers(input_list)












