# universal import
from universal_imports import *

# import features
import helper

#------------------------------

def get_cumulative_expenses_by_day_in_a_month(in_df, year, month, last_day = -1):
    """
    DESCRIPTION:
        - Tally the expense of the month cumulatively as of each day till the input last day
        - E. g. spent this much as of day 1, as of day 2, as of day 3, etc.

    INPUT SIGNATURE:
        1. in_df (pandas dataframe): the main dataframe
        2. year (int): the year
        3. month (int): the month
        4. last_day (int): the day

    OUTPUT SIGNATURE:
        1. month_trend_df (pandas dataframe): a dataframe with 2 columns: Date, Cumulative Expenses
        2. month_total (float): the total expense of the month
    """

    #------------------------------
    # 2 lists to combine into the final dataframe
    dates = []
    cumulative_expenses = []

    #------------------------------
    # Calculate the cumulative expenses as of each day

    # days in month dictionary
    days_in_month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # if day is not defined by the user, then set it to the last day of the month
    if last_day == -1:
        last_day = days_in_month_dict[month]

    # if the day is larger than the last day of the month, then set it to the last day of the month
    if last_day > days_in_month_dict[month]:
        last_day = days_in_month_dict[month]

    # loop through each day in the month until the stop date
    d = 1
    while d <= last_day:

        # format this day
        this_day = datetime.datetime(year = year, month = month, day = d)

        # if in the future, transactions' details also include time (hour, minute, second),
        # then we will need to find previous_day and next_day and fitler the transactions BETWEEN
        # previous_day and next_day

        # filter all the transactions in the day
        day_df = in_df [ (in_df['Date'] == this_day) ]

        # if this day doesn't exist in the main dataframe
        if len(day_df) == 0:
            
            dates.append(d)

            # add the total expense of the day to the total_so_far list
            if (len(cumulative_expenses) == 0):
                cumulative_expenses.append(0)
            else:
                cumulative_expenses.append(cumulative_expenses[-1])

        else:

            dates.append(d)

            # sum total expense of the day
            day_total = day_df['Amount'].sum()

            # add the total expense of the day to the total_so_far list
            if (len(cumulative_expenses) == 0):
                cumulative_expenses.append(day_total)
            else:
                cumulative_expenses.append(day_total + cumulative_expenses[-1])

        # increment the day
        d += 1

    #------------------------------
    # Create the dataframe

    # create the dataframe
    month_trend_df = pd.DataFrame({'Day': dates, 'Cumulative Expenses': cumulative_expenses})

    #------------------------------
    # total expense of the month
    month_total = cumulative_expenses[-1]

    return month_trend_df, month_total

#------------------------------

def graph_months_trend(in_df, year, month, last_day = -1):
    """
    DESCRIPTION:
        - Graph the cumulative expenses of the month as of each day till the input of last day
        - Graph both this month and last month on the same plot

    INPUT SIGNATURE:
        1. in_df (pandas dataframe): the main dataframe
        2. year (int): the year
        3. month (int): the month
        4. last_day (int): the end day

    OUTPUT SIGNATURE:
        1. graph_name (str): the name of the graph
    """

    #------------------------------
    # Get the cumulative expenses of this month and last month

    # get this month cumulative expenses
    this_month_trend_df = get_cumulative_expenses_by_day_in_a_month (
        in_df = in_df, \
        year = year, \
        month = month, \
        last_day = last_day)[0]

    # get last month cumulative expenses

    # if this month is January, then previous month is December of the previous year
    if month == 1:
        previous_month_trend_df = get_cumulative_expenses_by_day_in_a_month (
            in_df = in_df, \
            year = year - 1, \
            month = 12)[0]

    else:
        previous_month_trend_df = get_cumulative_expenses_by_day_in_a_month (
            in_df = in_df, \
            year = year, \
            month = month - 1)[0]

    #------------------------------
    # Graph the cumulative expenses of the month

    # clear figure
    plt.clf()

    months_plot = sns.lineplot(data = this_month_trend_df, x = 'Day', y = 'Cumulative Expenses')
    months_plot = sns.lineplot(data = previous_month_trend_df, x = 'Day', y = 'Cumulative Expenses')
    months_plot.set_xlabel("Day",fontsize = 15)
    months_plot.set_ylabel("Cumulative Expenses",fontsize = 15)
    plt.legend(labels=["This Month Trend","Last Month Trend"])

    #------------------------------
    # exporting the figure

    # get a unique id
    id = str(helper.get_unique_id())

    # generate a name
    name = 'months_trend_' + id + '.png'

    # generate the path
    path = 'Flask/static/' + name

    plt.savefig(path, dpi = 150, bbox_inches = 'tight')

    # delete all redundant figures
    helper.clean_up_all_but(\
        folder = "Flask/static/", \
        starts_with = 'months_trend_', \
        not_delete_id = id, \
        ends_with = ".png")

    return name

#------------------------------
