class data_store (object):

    """
    A class that store data as global variables to be used by other modules
    """
    def __init__(self):

        #------------------------------
        # user-dependent variables

        self.username = None
        self.main_df = None

        #------------------------------
        # time variables

        self.current_year = None
        self.current_month = None
        self.current_day = None
        self.current_date_str = None
        self.start_of_the_month_str = None

        #------------------------------
        # categorical variable

        self.category = None