# def find_most_common_word(filename):
#     word_count = {}
#     with open(filename, 'r') as file:
#         for line in file:
#             words = line.split()
#             for word in words:
#                 word_count[word] = word_count.get(word, 0) + 1
#     maxword = None
#     maxcount = None
#     for word, frequency in word_count.items():
#         if maxcount is None or frequency > maxcount :
#             maxword = word
#             maxcount = frequency
#     return (f"The most freq word is: {maxword}, and the freq is: {maxcount}.")
# print(find_most_common_word('iso.txt'))


# fobj= open('qan_stk_prc.csv', mode='rt')

# def main():
#     filename = r'C:\Users\user\PycharmProjects\toolkit\lectures\iso.txt'  # Change this to your file's name
#     most_common_word, frequency = find_most_common_word(filename)
#     if most_common_word:
#         print(f"The most common word is '{most_common_word}' with a frequency of {frequency}.")
#     else:
#         print("No words found in the file.")
#
#
# if __name__ == "__main__":
#     main()

# sample solution

import numpy as np
import pandas as pd


# import yfinance as yf # Uncomment this line if you are wish to work with `yfinance` outside of Ed
#
# # Write this function
# def fx_code(from_cur, to_cur):
#     """ Creates a string with the ticker required to download exchange rates
#     using yfinance. The exchange rate will be the price of one unit of the `from_cur` in terms
#     of the `to_cur`.
#
#     Parameters
#     ----------
#     from_cur : str
#         The ISO code of the currency to be priced.
#
#     to_cur : str
#         The ISO code of the currency with the value of one unit of `from_cur`.
#
#
#     Returns
#     -------
#         A string that meets the `yfinance` ticker standards with ALL characters in upper case.
#         The function should also be able to ignore leading and trailing spaces. For example,
#         " aud", "Aud ", and " AUD " all are treated as "AUD" internally. See the
#         Notes section below for more information.
#
#     Notes
#     -----
#     Yahoo finance uses the following naming rules to define the ticker of the
#     exchange rate AAA/BBB:
#     usd/aud
#
#     1. If AAA is the USD, then the ticker is "BBB=X", i.e., the second currency
#        code with "=X" added at the end.
#     2. If AAA is not the USD, then the ticker is "AAABBB=X"
#
#     For example, the ticker for AUD/USD is "AUDUSD=X", while the ticker for
#     USD/AUD is "AUD=X"
#
#     So, if `from_cur=AAA` and the `to_cur=BBB`, the YF ticker will be:
#     1. "BBB=X" if AAA is USD
#     2. "AAABBB=X" if AAA is not the USD
#     """
#
#     pass
#     from_cur = from_cur.strip().upper()
#     to_cur = to_cur.strip().upper()
#
#     if from_cur == 'USD':
#         return f"{to_cur}=X"
#     else:
#         return f"{from_cur}{to_cur}=X"
#
#
# # get_fx is provided to demonstrate how you can download currency data from `yfinance`.
# # Once your fx_code function above is correct, get_fx should work on a computer
# # that has the `yfinance` package installed.
# def get_fx(from_cur, to_cur, period=None, interval=None):
#     """ Downloads the exchange rate between the `from_cur` and the `to_cur`.
#     The exchange rate will be the price of one unit of the `from_cur` in terms
#     of the `to_cur`
#
#     Parameters
#     ----------
#     from_cur : str
#         The ISO code of the currency to be priced
#
#     to_cur : str
#         The ISO code of the currency with the value of one unit of
#         `from_cur`.
#
#     period : str, None
#         valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
#         (optional, default is '1mo')
#
#     interval : str, None
#         valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
#         (optional, default is '1d')
#
#     Returns
#     -------
#     df
#         Dataframe with daily exchange rates from Yahoo Finance
#
#     """
#     # Defaults
#     if period is None:
#         period = '1mo'
#     if interval is None:
#         interval = '1d'
#
#     tic = fx_code(from_cur, to_cur)
#
#     # fetches the data
#     df = yf.download(tic, period=period, interval=interval)
#
#     return df

import pandas as pd
import numpy as np


# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):
    """ Combines the information from different sources to produce a dataframe
    with dates row labels. Row labels must be sorted

    Parameters
    ----------
    date_info : list
        date_info = [(row_id, date)]

    aud_usd_info : list
        aud_usd_info = [(row_id, aud/usd)]


    eur_aud_info : list
        eur_aud_info = [(row_id, eur/aud)]

    Returns
    -------
    df
    """
    pass

    date_dic = dict(date_info)
    aud_usd_dic = dict(aud_usd_info)
    eur_aud_dic = dict(eur_aud_info)

    # Combine dictionaries to ensure all dates are present
    combined_dict = {date: {'AUD/USD': aud_usd_dic.get(row_id), 'EUR/AUD': eur_aud_dic.get(row_id)}
                     for row_id, date in date_info}

    # Create DataFrame from combined dictionary
    df = pd.DataFrame.from_dict(combined_dict, orient='index')

    # Sort DataFrame by index (dates)
    df.sort_index(inplace=True)

    return df


# Sample data for you to develop your function
# date_info = [(row_id, date)]
date_info = [
    (11, '2020-09-08'),
    (70, '2020-09-09'),
    (99, '2020-09-10'),
    (4, '2020-09-11'),
    (7, '2020-09-14'),
    (100, '2020-09-15'),
]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70, 0.7209),
    (4, 0.7263),
    (11, 0.7280),
    (7, 0.7281),
    (100, 0.7285),
]

# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70, 1.6321),
    (4, 1.6282),
    (99, 1.6221),
    (100, 1.6288),
    (11, 1.6232),
]

df = mk_df(date_info, aud_usd_info, eur_aud_info)
print(df)



