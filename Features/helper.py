# universal import
from universal_imports import *

#------------------------------

def datetime_convert(target_string):
    """
    DESCRIPTION
        Convert a simple YYYY-MM-DD HH:MM to a datetime object
    """

    return pd.to_datetime(target_string)

#------------------------------

def get_unique_id():
    """
    DESCRIPTION:
        Generate a unique ID (for each transaction)
        The idea is simple, convert the current datetime.now() into an integer

    OUTPUT SIGNATURE:
        1. unique_id (str): the unique ID
    """

    # built in delay to ensure the time is different
    time.sleep(0.000001)
    
    # get current time
    now = datetime.datetime.now()

    # convert to timestamp (seconds since 1970)
    now_float = now.timestamp()

    # convert to a unique integer
    now_int = int(now_float * 10**6)

    # string convert it to avoid scientific notation display
    now_str = str(now_int)

    return now_str

#------------------------------

def reformat_main_df(df):
    """
    DESCRIPTION:
        Reformat the main dataframe to be more readable

    INPUT SIGNATURE:
        1. df (pandas dataframe): the main dataframe

    OUTPUT SIGNATURE:
        1. df (pandas dataframe): the reformatted main dataframe
    """

    # convert "Unique ID" to string to avoid scientific notation display
    df['Unique ID'] = df['Unique ID'].astype(str)

    # convert the date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # convert the amount column to float
    df['Amount'] = df['Amount'].astype(float)

    # round all the amounts to 2 decimal places
    df['Amount'] = df['Amount'].round(2)

    return df

#------------------------------

def random_from_percentage(chance):
    """
    DESCRIPTION:
        Given an integer representing a percentage (0-100), return whether the event happened or not

    INPUT SIGNATURE:
        1. chance (int): the percentage chance of the event happening

    OUTPUT SIGNATURE:
        1. (bool): whether the event happened or not
    """

    # generate a random number
    random_number = random.randint(0, 100)

    # check if the event happened
    if random_number <= chance:
        return True
    else:
        return False

#------------------------------

def clean_up_all_but (folder, starts_with, not_delete_id, ends_with = ".png"):
    """
    DESCRIPTION:
        look into a folder, delete all files that starts with a certain name that does not have the "not-delete id"

    INPUT SIGNATURE:
        1. folder (str): the folder to look into (include the '/' at the end)
        2. starts_with (str): the start of the file name
        3. not_delete_id (str): the unique id of a file that should not be deleted
        4. ends_with (str): the end of the file name

    EXAMPLE:
        for the not-delete-file: "overall_graph_146143154145.png"
        starts_with is: "overall_graph_"
        not_delete_id is: "146143154145"
        ends_with is: ".png"

    REASON:
        Why use this method of generating files with unique names and delete old ones instead
        of simply overwriting the old ones?
        This is because a cache handling error in the browser, sometimes, the new image will not be
        loaded if the name is the same, even if the file is overwritten. This is a workaround.
    """

    # not_delete_file = folder + starts_with + not_delete_id + ends_with

    all_files_name = os.listdir(folder) # add the last / when using this function

    all_files_path = [] 
    for file_name in all_files_name:
        file_path = folder + file_name
        all_files_path.append(file_path)

    for file in all_files_path:

        if starts_with in file:

            if not_delete_id not in file:
                os.remove(file)