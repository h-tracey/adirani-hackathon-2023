# pylint: disable=no-member, import-error
from flask.views import MethodView
from services.analysis_engine import AnalysisEngine
from repos.data_driver import DataRepo
from os import getenv
from flask import request, send_file, jsonify


class TouchpointsCountView(MethodView):
    def __init__(
        self
    ) -> None:
        super().__init__() 
        self.__analysis = AnalysisEngine(DataRepo(getenv('SQL_URL')))
    def get(self):
        data = request.args.get('data', 'true') == 'true'
        raw = self.__analysis.touchpoints_count(not data)
        
        if data:
            return jsonify(dict(array=raw.to_dict('records')))
        else:
            return send_file("temp/image.png", mimetype='image/png', as_attachment=False)
