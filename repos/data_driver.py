from sqlalchemy import text
import pandas as pd
from sqlalchemy import create_engine

URL = 'mysql://root:example@host.docker.internal/analytics'


QUERY_MAP = {
    "con_per_p": "repos/sql_queries/conversions_per_page.sql",
    "prp_gnd": "repos/sql_queries/proportion_by_gender.sql",
    "agg_conn_type": "repos/sql_queries/conversions_per_type_aggregated.sql",
    "prp_intr": "repos/sql_queries/proportion_by_intersts.sql",
    "prp_cnt": "repos/sql_queries/conversions_proportion_by_country.sql",
    "prp_lang": "repos/sql_queries/proportion_by_language.sql",
    "tp_conv": "repos/sql_queries/number_of_touchpoints_per_conversion.sql",
    "chan_conv": "repos/sql_queries/total_conversions_per_channel.sql",
    "prp_age": "repos/sql_queries/proportion_by_age.sql"}


class DataRepo():
    def __init__(self, sql_url):
        self.con = create_engine(sql_url)

    def __get_data(self, query):
        sql_qry = QUERY_MAP[query]
        with open(sql_qry) as file:
            query = text(file.read())
            try:
                return pd.read_sql_query(query, con=self.con)
            except Exception as err:
                print(err)
                raise

    @property
    def get_conversions_per_num_touchpoints(self) -> pd.DataFrame:
        return self.__get_data('tp_conv')

    @property
    def get_conversions_per_page(self) -> pd.DataFrame:
        return self.__get_data('con_per_p')

    @property
    def get_conversions_per_type_agg(self) -> pd.DataFrame:
        return self.__get_data('agg_conn_type')

    @property
    def get_conversions_per_channel(self) -> pd.DataFrame:
        return self.__get_data('chan_conv')
