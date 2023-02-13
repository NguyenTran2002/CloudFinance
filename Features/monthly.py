# universal import
from universal_imports import *

# import features
import helper

#------------------------------

def get_cumulative_expenses_by_day_in_a_month(in_df, year, month):
    """
    DESCRIPTION:
        - Tally the expense of the month cumulatively as of each day
        - E. g. spent this much as of day 1, as of day 2, as of day 3, etc.

    INPUT SIGNATURE:
        1. in_df (pandas dataframe): the main dataframe
        2. year (int): the year
        3. month (int): the month

    OUTPUT SIGNATURE:
        1. month_trend_df (pandas dataframe): a dataframe with 2 columns: Date, Cumulative Expenses
    """

    #------------------------------
    # 2 lists to combine into the final dataframe
    dates = []
    cumulative_expenses = []

    #------------------------------
    # Get the start and end date of the month

    # get the start date of the month
    start_date = datetime.datetime(year = year, month = month, day = 1)

    # days in month dictionary
    days_in_month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    for d in range(1, days_in_month_dict[month] + 1):

        dates.append(d)

        # format this day
        this_day = datetime.datetime(year = year, month = month, day = d)

        # check if this day exist in the main dataframe
        if this_day not in in_df['Date'].unique():
            continue

        else:

            # filter all the transactions in the day
            day_df = in_df [ (in_df['Date'] == this_day) ]

            # sum total expense of the day
            day_total = day_df['Amount'].sum()

            # add the total expense of the day to the total_so_far list
            if d == 1:
                cumulative_expenses.append(day_total)
            else:
                cumulative_expenses.append(day_total + cumulative_expenses[-1])

    #------------------------------
    # Create the dataframe

    # create the dataframe
    month_trend_df = pd.DataFrame({'Day': dates, 'Cumulative Expenses': cumulative_expenses})

    return month_trend_df