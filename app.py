# navigate to the Features folder
import sys
sys.path.append(sys.path[0]+'/./Features')

# UNIVERSAL IMPORT
from universal_imports import *

#------------------------------

# import features
import category_module
import data_store
import helper
import monthly
import yearly
import data_manipulation

#------------------------------

# initialize the data_store object
global_data = data_store.data_store()

#------------------------------

# FLASK APP

app = flask.Flask(__name__, template_folder = 'Flask/templates', static_folder = 'Flask/static')

#------------------------------

@app.route("/", methods=['GET', 'POST'])
def index():

    # global variables in use
    global global_data

    #------------------------------
    # User and data

    # hardcode the username
    global_data.username = 'Nguyen'

    # read in the main dataframe
    global_data.main_df = pd.read_csv('Data/Expenses.csv')

    # reformat the main dataframe
    global_data.main_df = helper.reformat_main_df(global_data.main_df)

    #------------------------------
    # Break-down of This Month Expenses

    # get the current year, month, day
    global_data.current_year = datetime.datetime.now().year
    global_data.current_month = datetime.datetime.now().month
    global_data.current_day = datetime.datetime.now().day
    global_data.current_date_str = str(global_data.current_year) + \
        '-' + str(global_data.current_month) + \
        '-' + str(global_data.current_day)
    global_data.start_of_the_month_str = str(global_data.current_year) + \
        '-' + str(global_data.current_month) + '-01'

    # graph the total expenses for each category
    graph_sum_ALL_category_name = category_module.graph_sum_categories( \
        in_df = global_data.main_df, \
        start_time = global_data.start_of_the_month_str, \
        end_time = global_data.current_date_str)

    # generate URL for the graph from file name
    graph_sum_ALL_category_URL = flask.url_for('static',\
        filename =  graph_sum_ALL_category_name)

    #------------------------------

    return flask.render_template('index.html', \
        username = global_data.username, \
        today = global_data.current_date_str, \
        sum_ALL_categories_plot = graph_sum_ALL_category_URL)

#------------------------------

@app.route("/add_transaction", methods=['GET', 'POST'])
def add_transaction():
    """
    DESCRIPTION:
        Provide the user with a form interface to add a new transaction
        The transaction will be added when the submit button is clicked,
            which redirect the user to the route /transaction_added
    """

    # global variables in use
    global global_data

    # get the list of categories
    categories = global_data.main_df['Category'].unique().tolist()

    # get the list of all accounts
    accounts = global_data.main_df['Account'].unique().tolist()

    # sort both lists from A to Z
    categories.sort()
    accounts.sort()

    return flask.render_template('add_transaction.html',
        categories = categories,
        accounts = accounts)

#------------------------------

@app.route("/transaction_added", methods=['GET', 'POST'])
def transaction_added():
    """
    DESCRIPTION:
        Add a new transaction with the user inputted data
    """

    # global variables in use
    global global_data

    # # request the user inputted data
    # description = flask.request.form.get('description')
    # category = flask.request.form.get('category')
    # amount = flask.request.form.get('amount')
    # date = flask.request.form.get('date')
    # account = flask.request.form.get('account')
    # third_party = flask.request.form.get('third_party')


    description = flask.request.args.get('description')
    category = flask.request.args.get('category')
    amount = flask.request.args.get('amount')
    date = flask.request.args.get('date')
    account = flask.request.args.get('account')
    third_party = flask.request.args.get('third_party')

    # add the new transaction to the main dataframe
    global_data.main_df, new_transaction_df = data_manipulation.add_transaction(
        in_df = global_data.main_df,
        description = description,
        category = category,
        amount = amount,
        date = date,
        account = account,
        third_party = third_party)

    # save the main dataframe to the csv file
    global_data.main_df.to_csv('Data/Expenses.csv', index = False)

    #------------------------------

    return flask.render_template('transaction_added.html',
        new_transaction_df_html = [new_transaction_df.to_html(classes = 'new_transaction_df', header = "true")])

#------------------------------

@app.route("/months_trend", methods=['GET', 'POST'])
def months_trend():

    # global variables in use
    global global_data

    #------------------------------
    # Comparing This Month Trend to Last Month Trend

    graph_months_trend_name = monthly.graph_months_trend( \
        in_df = global_data.main_df, \
        year = global_data.current_year, \
        month = global_data.current_month, \
        last_day = global_data.current_day)

    # generate URL for the graph from file name
    graph_months_trend_URL = flask.url_for('static',\
        filename =  graph_months_trend_name)


    return flask.render_template('months_trend.html', \
        months_trend_plot = graph_months_trend_URL)

#------------------------------

@app.route("/years_trend", methods=['GET', 'POST'])
def years_trend():

    # global variables in use
    global global_data

    #------------------------------
    # Comparing This Year Trend to Last Year Trend

    graph_years_trend_name = yearly.graph_years_trend( \
        in_df = global_data.main_df, \
        year = global_data.current_year, \
        last_month = global_data.current_month, \
        last_day = global_data.current_day)

    # generate URL for the graph from file name
    graph_years_trend_URL = flask.url_for('static',\
        filename = graph_years_trend_name)


    return flask.render_template('years_trend.html', \
        years_trend_plot = graph_years_trend_URL)

#------------------------------

@app.route("/single_category", methods=['GET', 'POST'])
def single_category():

    # global variables in use
    global global_data

    #------------------------------
    # request the category name from URL
    category = flask.request.args.get('category')

    # store the category globally
    global_data.category = category

    #------------------------------
    # get the total spent of the category and the filtered dataframe
    category_total, category_df = category_module.sum_category(\
        in_df = global_data.main_df, \
        category = category, \
        start_time = global_data.start_of_the_month_str, \
        end_time = global_data.current_date_str)

    #------------------------------

    return flask.render_template('single_category.html', \
        category = category, \
        start_date = global_data.start_of_the_month_str, \
        end_date = global_data.current_date_str, \
        total_expenses = category_total, \
        category_df_html = [category_df.to_html(classes = 'category_df', header = "true")])

#------------------------------

@app.route("/single_category_alt_date", methods=['GET', 'POST'])
def single_category_alt_date():

    # global variables in use
    global global_data

    #------------------------------
    # request the category name, start date, and end date from URL
    category = global_data.category
    start_date = flask.request.args.get('start_date')
    end_date = flask.request.args.get('end_date')

    #------------------------------
    # get the total spent of the category and the filtered dataframe
    category_total, category_df = category_module.sum_category(\
        in_df = global_data.main_df, \
        category = category, \
        start_time = start_date, \
        end_time = end_date)

    #------------------------------

    return flask.render_template('single_category.html', \
        category = category, \
        start_date = start_date, \
        end_date = end_date, \
        total_expenses = category_total, \
        category_df_html = [category_df.to_html(classes = 'category_df', header = "true")])

#------------------------------
if __name__ == '__main__':

    app.run(debug = False, port = 2700)