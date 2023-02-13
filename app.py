# navigate to the Features folder
import sys
sys.path.append(sys.path[0]+'/./Features')

# UNIVERSAL IMPORT
from universal_imports import *

#------------------------------

# import features
import helper
import category_module

#------------------------------

# FLASK APP

app = flask.Flask(__name__, template_folder = 'Flask/templates', static_folder = 'Flask/static')

@app.route("/", methods=['GET', 'POST'])
def index():

    # read in the main dataframe
    main_df = pd.read_csv('Data/Expenses.csv')

    # reformat the main dataframe
    main_df = helper.reformat_main_df(main_df)

    # graph the total expenses for each category
    graph_sum_ALL_category_name = category_module.graph_sum_categories( \
        in_df = main_df, \
        start_time = '2023-01-01', \
        end_time = '2023-01-31')

    # generate URL for the graph from file name
    graph_sum_ALL_category_URL = flask.url_for('static',\
        filename =  graph_sum_ALL_category_name)

    return flask.render_template('index.html', \
        sum_ALL_categories_plot = graph_sum_ALL_category_URL)


#------------------------------
if __name__ == '__main__':

    app.run()