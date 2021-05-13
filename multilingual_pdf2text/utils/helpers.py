from datetime import datetime, timedelta
from dateutil.relativedelta import *
from linkedin_jobs_pyscraper.search.search_jobs import Search
import pandas as pd
from linkedin_jobs_pyscraper.models.filters.filters import  FilterMap


def get_search_instance(searcher, filters):
    """
    Creates search instance for running the search on LinkedIn.
    Keyword arguments:
    config -- pydantic model
    """
    ## create searcher model & create dict filter with map
    filter_map = FilterMap()
    filter_map_dict = filter_map.__dict__
    filters_dict = filters.__dict__
    str_filter = ''
    for map_key, filter_key in  zip(sorted(filter_map_dict.keys()), sorted(filters_dict.keys())):
       str_filter += '&{}={}'.format(filter_map_dict[map_key], filters_dict[filter_key].value )
    
    searcher.search_url = searcher.search_url + str_filter

    return Search(searcher)    ## return instantiated searcher object
    

def write_to_file(data, batch_number, file_path):
    """
    Writer list of dictionaries to csv using Pandas.
    Keyword arguments:
    data -- list, list of dictionaries to be written on file.
    batch_number -- 
    file_path -- output file path
    """
    df = pd.DataFrame(data, columns=data[0].keys())
    if batch_number > 0:
        df.to_csv(file_path, mode='a', header=False)
    else:
        df.to_csv(file_path)

def rel_time_to_absolute_datetime(relative_time_str):
    """
    Writer list of dictionaries to csv using Pandas.
    Keyword arguments:
    data -- list, list of dictionaries to be written on file.
    batch_number -- 
    file_path -- output file path
    """
    N = int(relative_time_str.split(' ')[0])
    date_n_days_ago = None
    if 'day' in relative_time_str:
        date_n_days_ago = datetime.now() - timedelta(days=N)
    elif 'week' in relative_time_str:
        date_n_days_ago = datetime.now() - relativedelta(months=-N)
    elif 'hours' in relative_time_str:
        date_n_days_ago = datetime.now() - relativedelta(hours=-N)
    elif 'month' in relative_time_str:
        date_n_days_ago = datetime.now() - relativedelta(months=-N)
    return str(date_n_days_ago).split(' ')[0]


