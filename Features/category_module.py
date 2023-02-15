# universal import
from universal_imports import *

# import features
import helper

#------------------------------

def sum_category(in_df, category, start_time = '1900-01-01', end_time = '2200-12-31'):
    """
    DESCRIPTION:
        Sum the category over the time period

    INPUT SIGNATURE:
        1. in_df (pd.DataFrame): the input dataframe
        2. category (str): the category to sum
        3. start_time (string): YYYY-MM-DD format
        4. end_time (string): YYYY-MM-DD format

    OUTPUT SIGNATURE:
        1. category_sum (float): the sum of the category over the time period
        2. filtered_df (pd.DataFrame): the filtered dataframe
    """

    # convert start_time and end_time to datetime
    start_time = pd.to_datetime(start_time)
    end_time = pd.to_datetime(end_time)

    # filter the dataframe
    filtered_df = in_df[(in_df["Date"] >= start_time) & (in_df["Date"] <= end_time)\
        & (in_df["Category"] == category)]

    # sum the category
    category_sum = filtered_df["Amount"].sum()

    return category_sum, filtered_df

#------------------------------

def sum_ALL_categories(in_df, start_time = '1900-01-01', end_time = '2200-12-31'):

    """
    DESCRIPTION:
        Sum all the categories over the time period

    INPUT SIGNATURE:
        1. in_df (pd.DataFrame): the input dataframe
        2. start_time (string): YYYY-MM-DD format
        3. end_time (string): YYYY-MM-DD format

    OUTPUT SIGNATURE:
        1. sum_categories (dict): a dictionary of the total amount spent in each category
        2. sum_categories_df (pd.DataFrame): a dataframe of the total amount spent in each category
    """

    # convert start_time and end_time to datetime
    start_time = pd.to_datetime(start_time)
    end_time = pd.to_datetime(end_time)

    # filter the dataframe
    filtered_df = in_df[(in_df["Date"] >= start_time) & (in_df["Date"] <= end_time)]

    # get the unique categories
    categories = filtered_df.Category.unique()

    # create a dictionary to store the total amount spent in each category
    sum_categories = {}

    # loop through the categories
    for category in categories:

        # sum the category
        category_sum = sum_category(filtered_df, category, start_time, end_time)[0]

        # add the category and sum to the dictionary
        sum_categories[category] = category_sum

    # convert the dictionary to a dataframe
    sum_categories_df = pd.DataFrame(sum_categories.items(), columns = ['Category', 'Amount'])

    # sort the dictionary in descending order
    sum_categories_df = sum_categories_df.sort_values(by = 'Amount', ascending = False)

    return sum_categories, sum_categories_df

#------------------------------

def graph_sum_categories(in_df, start_time = '1900-01-01', end_time = '2200-12-31'):
    """
    DESCRIPTION:
        Graph the total amount spent in each category over the time period
        Export the graph in Flask/static/images

    INPUT SIGNATURE:
        1. in_df (pd.DataFrame): the input dataframe
        2. start_time (string): YYYY-MM-DD format
        3. end_time (string): YYYY-MM-DD format

    OUTPUT SIGNATURE:
        1. name (str): the filename of the exported graph
    """

    #------------------------------
    # tally the necessary data
    categories_df = sum_ALL_categories(in_df, start_time, end_time)[1]

    #------------------------------
    # creating the figure

    # clear figure
    plt.clf()

    # create the bar chart
    plt.xticks(rotation=45)
    ax = sns.barplot(x = 'Category', y = 'Amount', data = categories_df)
    ax.set_xlabel("Category",fontsize = 15)
    ax.set_ylabel("Expenses",fontsize = 15)

    # shows value on top of each bar
    for i in ax.containers:
        ax.bar_label(i,)

    #------------------------------
    # exporting the figure

    # get a unique id
    id = str(helper.get_unique_id())

    # generate a name
    name = 'sum_categories_' + id + '_' + start_time + '_' + end_time + '.png'

    # generate the path
    path = 'Flask/static/' + name

    ax.figure.savefig(path, dpi = 150, bbox_inches = 'tight')

    # delete all redundant figures
    helper.clean_up_all_but(\
        folder = "Flask/static/", \
        starts_with = 'sum_categories_', \
        not_delete_id = id, \
        ends_with = ".png")

    return name

