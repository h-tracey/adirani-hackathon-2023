from sqlalchemy import text
from engine import get_engine
import pandas as pd

QUERY_MAP = {
    "con_per_p": "sql_queries/conversions_per_page.sql",
    "prp_gnd": "sql_queries/proportion_by_gender.sql",
    "agg_conn_type": "sql_queries/conversions_per_type_aggregated.sql",
    "prp_intr": "sql_queries/proportion_by_intersts.sql",
    "prp_cnt": "sql_queries/conversions_proportion_by_country.sql",
    "prp_lang": "sql_queries/proportion_by_language.sql",
    "tp_conv": "sql_queries/number_of_touchpoints_per_conversion.sql",
    "chan_conv": "sql_queries/total_conversions_per_channel.sql",
    "prp_age": "sql_queries/proportion_by_age.sql"}


class DataFetch():
    def __init__(self):
        self.con = get_engine()

    def get_data(self, query):
        sql_qry = QUERY_MAP[query]
        with open(sql_qry) as file:
            query = text(file.read())
            return pd.read_sql_query(query, con=self.con)
