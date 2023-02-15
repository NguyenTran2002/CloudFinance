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
    current_date_str = str(global_data.current_year) + \
        '-' + str(global_data.current_month) + \
        '-' + str(global_data.current_day)
    start_of_the_month_str = str(global_data.current_year) + \
        '-' + str(global_data.current_month) + '-01'

    # graph the total expenses for each category
    graph_sum_ALL_category_name = category_module.graph_sum_categories( \
        in_df = global_data.main_df, \
        start_time = start_of_the_month_str, \
        end_time = current_date_str)

    # generate URL for the graph from file name
    graph_sum_ALL_category_URL = flask.url_for('static',\
        filename =  graph_sum_ALL_category_name)

    #------------------------------

    return flask.render_template('index.html', \
        username = global_data.username, \
        today = current_date_str, \
        sum_ALL_categories_plot = graph_sum_ALL_category_URL)

#------------------------------

@app.route("/trend", methods=['GET', 'POST'])
def trend():

    # global variables in use
    global global_data

    #------------------------------
    # Comparing This Month Trend to Last Month Trend

    graph_months_trend_name = monthly.graph_months_trend( \
        in_df = global_data.main_df, \
        year = global_data.current_year, \
        month = global_data.current_month)

    # generate URL for the graph from file name
    graph_months_trend_URL = flask.url_for('static',\
        filename =  graph_months_trend_name)


    return flask.render_template('trend.html', \
        months_trend_plot = graph_months_trend_URL)

#------------------------------

#------------------------------
if __name__ == '__main__':

    app.run()