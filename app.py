# navigate to the Features folder
import sys
sys.path.append(sys.path[0]+'/./Features')

# UNIVERSAL IMPORT
from universal_imports import *

#------------------------------

# import features
import helper
import category_module
import monthly

#------------------------------

# FLASK APP

app = flask.Flask(__name__, template_folder = 'Flask/templates', static_folder = 'Flask/static')

@app.route("/", methods=['GET', 'POST'])
def index():

    # read in the main dataframe
    main_df = pd.read_csv('Data/Expenses.csv')

    # reformat the main dataframe
    main_df = helper.reformat_main_df(main_df)

    #------------------------------
    # Break-down of This Month Expenses

    # get the current year, month, day
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day
    current_date_str = str(current_year) + '-' + str(current_month) + '-' + str(current_day)
    start_of_the_month_str = str(current_year) + '-' + str(current_month) + '-01'

    # graph the total expenses for each category
    graph_sum_ALL_category_name = category_module.graph_sum_categories( \
        in_df = main_df, \
        start_time = start_of_the_month_str, \
        end_time = current_date_str)

    # generate URL for the graph from file name
    graph_sum_ALL_category_URL = flask.url_for('static',\
        filename =  graph_sum_ALL_category_name)

    #------------------------------
    # Comparing This Month Trend to Last Month Trend

    graph_months_trend_name = monthly.graph_months_trend( \
        in_df = main_df, \
        year = current_year, \
        month = current_month)

    # generate URL for the graph from file name
    graph_months_trend_URL = flask.url_for('static',\
        filename =  graph_months_trend_name)


    return flask.render_template('index.html', \
        today = current_date_str, \
        sum_ALL_categories_plot = graph_sum_ALL_category_URL, \
        months_trend_plot = graph_months_trend_URL)


#------------------------------
if __name__ == '__main__':

    app.run()