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