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
    main_df = helper.reformat_df(main_df)

    # get the total expenses in each category
    category_sum_df = category_module.sum_ALL_categories(main_df)[1]

    return flask.render_template('index.html')


#------------------------------
if __name__ == '__main__':

    app.run()