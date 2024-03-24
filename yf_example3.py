""" yf_example3.py
Example of a function to download stock prices from Yahoo Finance.
"""

import os
import toolkit_config as cfg
import yf_example2


def qan_prc_to_csv(year):
    """
    This function takes a single (mandatory) parameter called year, an integer.

    Purpose: Download Qantas stock prices for a given year into a CSV file.

    The name of this file will be qan_prc_YYYY.csv, where the YYYY stands for the year.

    This file will be saved under the data folder. The location of this folder is already
    defined in the toolkit_config module.
    """
    start = f"{year}-01-01"
    end = f"{year}-12-31"
    filename = f"qan_prc_{year}.csv"
    pth = os.path.join(cfg.DATADIR, filename)
    dt = yf_example2.yf_prc_to_csv(tic='QAN.AX', start=start, end=end, pth=pth)


if __name__ == "__main__":
    # Test case
    qan_prc_to_csv(year=2020)
