# happy = 4
# if happy:
#     print("I am happy")

# var1 = "a"
# var2 = "a"
# var3 = ['a']
# var4 = ['a']
#
# print(var3 == var4)

# working_hours = float(input('type your working hours:' ))
# low_rate = 51.45
# high_rate =88.9
# if working_hours >= 35:
#     weekly_pay = high_rate * working_hours;
# elif working_hours <= 35:
#     weekly_pay = low_rate * working_hours
# print(f'The weekly pay is equal to {weekly_pay} dollars.')

# import yfinance
#
# start = '2020-01-01'
#
# end = None
#
# tickers = ["QAN.AX", "WES.AX"]
#
# for tic in tickers:
#     df = yfinance.download(tic, start, end, ignore_tz=True)
#
#     tic_base = tic.lower().split('.')[0]
#
#     df.to_csv(f'{tic_base}_stk_prc.csv')

# d = {
#
#     "beauty": True,
#
#     "truth": True,
#
#     "red wheelbarrow": 100000,
#
#     5: "fingers",
#
# }
# # for val in d.values():
# #     print(val)
#
# for key,value in d.items():
#
#     print(f'key :{key} value:{value}')

# for i in range(0,10,2):
#
#     print(f'i is now {i}')

# for i in range(5,0,-1):
#
#     print("This message will self-destruct in {} secs...".format(i))

# letters = ["a", "b", "c", "d", "e"]
#
# for i, x in enumerate(letters):
#     print(f"letters[{i}] --> {x}")

# numbers = [-2,3,9,1,5,7,2,11,0,3,12,3,15,10]
# max_num = numbers[0]
# for num in numbers:
#     if max_num < num:
#         max_num = num
# print(f"The largest value in the numbers is {max_num}.")

# years = [2018, 2019, 2020]
#
# months = [
#
#     "Jan",
#
#     "Feb",
#
#     "Mar",
#
#     "Apr",
#
#     "May",
#
#     "Jun",
#
#     "Jul",
#
#     "Aug",
#
#     "Sep",
#
#     "Oct",
#
#     "Nov",
#
#     "Dec",
# ]
#
# for month in months:
#     for year in years:
#         print("Month: {}, Year: {}".format(month, year))

# for x in range(1, 4):
#     for y in range(1, 4):
#         if x <= y:
#             print(x, y)

# for even in range(0,10,2):
#     print(even)
#     if even > 2:
#         continue

# l = ["Fairfield",
#     "Fairfield East",
#     "Fairfield Heights",
#     "Fairfield West",
#     "Fairlight",
#     "Fiddletown",
#     "Five Dock",
#     "Flemington",
#     "Forest Glen",
#     "Forest Lodge",
#     "Forestville",
#     "Freemans Reach",
#     "Frenchs Forest",
#     "Freshwater"]
#
# for n in l:
#     if n[0:6] != "Forest":
#         print(n)

# f_suburbs = dict()
# f_suburbs["Fairfield"] = 18081
# f_suburbs["Fairfield East"] = 5273
# f_suburbs["Fairfield Heights"] = 7517
# f_suburbs["Fairfield West"] = 11575
# f_suburbs["Fairlight"] = 5840
# f_suburbs["Fiddletown"] = 233
# f_suburbs["Five Dock"] = 9356
# f_suburbs["Flemington"] = None
# f_suburbs["Forest Glen"] = None
# f_suburbs["Forest Lodge"] = 4583
# f_suburbs["Forestville"] = 8329
# f_suburbs["Freemans Reach"] = 1973
# f_suburbs["Frenchs Forest"] = 13473
# f_suburbs["Freshwater"] = 8866
#
# for key,value in f_suburbs.items():
#     if key[0:6] != "Forest" and value is not None:
#         print(f"{key}:{value}")

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 != 0:
#         print (f"{i}: Fizz");
#     elif i % 5 == 0 and i % 3 != 0:
#         print (f"{i}: Buzz");
#     elif i % 3 == 0 and i % 5 == 0:
#         print (f"{i}: FIZZ BUZZ");
#     else:
#         print(i)

# l = ["Fairfield",
#     "Fairfield East",
#     "Fairfield Heights",
#     "Fairfield West",
#     "Fairlight",
#     "Fiddletown",
#     "Five Dock",
#     "Flemington",
#     "Forest Glen",
#     "Forest Lodge",
#     "Forestville",
#     "Freemans Reach",
#     "Frenchs Forest",
#     "Freshwater"]
# for i,x in enumerate(l):
#     print(f"{i}: {x}")

# first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
# middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
# last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']

# for z in last_names:
#     pass
#     for x in first_names:
#         pass
#         for y in middle_names:
#             if y is not None:
#                 print(f"{x} {y} {z}")
#             elif y is None:
#                 print(f"{x} {z}")