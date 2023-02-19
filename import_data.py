# pylint: disable=no-member, import-error
import re
from datetime import datetime, timedelta
import os
import pandas as pd
from repos.engine import get_engine
from sqlalchemy.exc import OperationalError

def filename_details(file: str):
    date_extract = re.compile('(?P<before>\d{4}-\d{2}-\d{2}) to (?P<after>\d{4}-\d{2}-\d{2})')
    name_extract = re.compile('(^[^\d]+)')
    match = date_extract.search(file)
    start = datetime.strptime(match['before'], '%Y-%m-%d')
    end = datetime.strptime(match['after'], '%Y-%m-%d')
    name = name_extract.match(file)[0].strip().replace(' - ', '_').replace(' ', '_')

    return dict(start=start, end=end, name=name)

def wrangle_dates(data_frame, details):

    def day_function(day_row, data_start):
        delta = timedelta(days=day_row)
        return data_start + delta

    if 'Product Revenue' in data_frame.columns:

        data_frame['Product Revenue'] = data_frame['Product Revenue'] \
        .str.replace('$', '') \
        .str.replace(',', '') \
        .astype(float)

    if 'Avg. Price' in data_frame.columns:

        data_frame['Avg. Price'] = data_frame['Avg. Price'] \
        .str.replace('$', '') \
        .str.replace(',', '') \
        .astype(float)

    if 'by_day' in details['name']:
        if 'Nth day' in data_frame.columns:
            data_frame['date'] = data_frame['Nth day'].apply(day_function, args=(details['start'],))
        else:
            data_frame['date'] = pd.to_datetime(data_frame['Day Index'])

    return data_frame

if __name__  == '__main__':
    directory = os.fsencode('data_clean')

    df_arr = []
    details_arr = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        f_name = os.fsdecode(file)
        path = f'{os.fsdecode(directory)}/{f_name}'
        file_details = filename_details(f_name)
        df = pd.read_excel(path)
        complete_df = wrangle_dates(df, file_details)
        df_arr.append(complete_df)
        details_arr.append(file_details)

    with get_engine() as sql_con:
        for i, df in enumerate(df_arr):
            print(details_arr[i]['name'])
            try:
                df.to_sql(details_arr[i]['name'], con=sql_con, if_exists='replace')
            except OperationalError as err:
                print(err)
                continue
        