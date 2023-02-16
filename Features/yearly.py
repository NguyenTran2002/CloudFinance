# universal import
from universal_imports import *

# import features
import helper
import monthly

#------------------------------

def get_cumulative_expenses_by_day_in_a_year(in_df, year, last_month = -1, last_day = -1):
    """
    DESCRIPTION:
        - Tally the expense of the month cumulatively as of each day till the input last month and last day
        - E. g. spent this much as of day 1, as of day 2, as of day 3, etc.

    INPUT SIGNATURE:
        1. in_df (pandas dataframe): the main dataframe
        2. year (int): the year
        3. last_month (int): the month
        4. last_day (int): the day

    OUTPUT SIGNATURE:
        1. month_trend_df (pandas dataframe): a dataframe with 2 columns: Date, Cumulative Expenses
    """

    #------------------------------
    # 2 lists to combine into the final dataframe
    months = []
    cumulative_expenses = []

    #------------------------------
    # Calculate the cumulative expenses as of each month

    # if day is not defined by the user, then set it to the last day of the month
    if last_month == -1:
        last_month = 12

    # if the day is larger than the last day of the month, then set it to the last day of the month
    if last_month > 12:
        last_month = 12

    # loop through each month in the year until the stop date
    m = 1
    while m <= last_month:

        months.append(m)

        # get the cumulative expenses as of the month
        month_expenses = \
            monthly.get_cumulative_expenses_by_day_in_a_month(in_df, year, m, last_day)[1]

        if len(cumulative_expenses) == 0:
            cumulative_expenses.append(month_expenses)

        else:
            cumulative_expenses.append(cumulative_expenses[-1] + month_expenses)

        # increment the month
        m += 1

    #------------------------------
    # Create the dataframe

    # create the dataframe
    year_trend_df = pd.DataFrame({'Month': months, 'Cumulative Expenses': cumulative_expenses})

    #------------------------------
    # total expenses in the year

    year_total = cumulative_expenses[-1]

    return year_trend_df, year_total

#------------------------------

def graph_years_trend(in_df, year, last_month = -1, last_day = -1):
    """
    DESCRIPTION:
        - Graph the cumulative expenses of the month as of each day till the input last month and last day
        - Graph both this month and last month on the same plot

    INPUT SIGNATURE:
        1. in_df (pandas dataframe): the main dataframe
        2. year (int): the year
        3. last_month (int): the end month
        4. last_day (int): the end day

    OUTPUT SIGNATURE:
        1. graph_name (str): the name of the graph
    """

    #------------------------------
    # Get the cumulative expenses of this month and last month

    # get this month cumulative expenses
    this_year_trend_df = get_cumulative_expenses_by_day_in_a_year (
        in_df = in_df, \
        year = year, \
        last_month = last_month, \
        last_day = last_day)[0]

    # get last month cumulative expenses

    previous_year_trend_df = get_cumulative_expenses_by_day_in_a_year (
        in_df = in_df, \
        year = year - 1)[0]

    #------------------------------
    # Graph the cumulative expenses of the year

    # clear figure
    plt.clf()

    years_plot = sns.lineplot(data = this_year_trend_df, x = 'Month', y = 'Cumulative Expenses')
    years_plot = sns.lineplot(data = previous_year_trend_df, x = 'Month', y = 'Cumulative Expenses')
    years_plot.set_xlabel("Month",fontsize = 15)
    years_plot.set_ylabel("Cumulative Expenses",fontsize = 15)
    plt.legend(labels=["This Year Trend","Previous Year Trend"])

    #------------------------------
    # exporting the figure

    # get a unique id
    id = str(helper.get_unique_id())

    # generate a name
    name = 'years_trend_' + id + '.png'

    # generate the path
    path = 'Flask/static/' + name

    plt.savefig(path, dpi = 150, bbox_inches = 'tight')

    # delete all redundant figures
    helper.clean_up_all_but(\
        folder = "Flask/static/", \
        starts_with = 'years_trend_', \
        not_delete_id = id, \
        ends_with = ".png")

    return name

#------------------------------
