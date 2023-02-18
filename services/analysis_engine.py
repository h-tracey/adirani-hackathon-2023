from repos.data_driver import DataRepo
import pandas as pd

class AnalysisEngine:
    def __init__(self, repo=DataRepo) -> None:
        self.repo = repo

    def calculate_page_conversions(self):
        page_data = self.repo.get_conversions_per_page
        agg_data = self.repo.get_conversions_per_type_agg

        return agg_data


