# pylint: disable=no-member, import-error
from flask import render_template
from flask.views import MethodView
from services.analysis_engine import AnalysisEngine
from repos.data_driver import DataRepo
from os import getenv


class ConversionView(MethodView):
    def __init__(
        self
    ) -> None:
        super().__init__() 
        self.__analysis = AnalysisEngine(DataRepo(getenv('SQL_URL')))

    def get(self):
        data  = self.__analysis.calculate_page_conversions()
        return render_template(
            'template.html',
            tables=[data.to_html(classes='data', header="true")]
        )
