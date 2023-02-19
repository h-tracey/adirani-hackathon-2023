# pylint: disable=no-member, import-error
from flask import render_template
from flask.views import MethodView
from services.analysis_engine import AnalysisEngine
from repos.data_driver import DataRepo
from os import getenv
from flask import request, send_file, jsonify


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

class ScatterTypeView(MethodView):
    def __init__(
        self
    ) -> None:
        super().__init__()
        self.__analysis = AnalysisEngine(DataRepo(getenv('SQL_URL')))

    def get(self):

        data = request.args.get('data', 'true') == 'true'

        raw = self.__analysis.scatter_conversion_rate_type(not data)
        if data:
            return jsonify(dict(array=raw.to_dict('records')))
        else:
            return send_file("temp/image.png", mimetype='image/png', as_attachment=False)

class ScatterView(MethodView):
    def __init__(
        self
    ) -> None:
        super().__init__()
        self.__analysis = AnalysisEngine(DataRepo(getenv('SQL_URL')))

    def get(self):

        data = request.args.get('data', 'true') == 'true'

        raw = self.__analysis.hexbin_conversion_rate(not data)
        if data:
            return jsonify(dict(array=raw.to_dict('records')))
        else:
            return send_file("temp/image.png", mimetype='image/png', as_attachment=False)

class BoxViewsView(MethodView):
    def __init__(
        self
    ) -> None:
        super().__init__()
        self.__analysis = AnalysisEngine(DataRepo(getenv('SQL_URL')))

    def get(self):

        data = request.args.get('data', 'true') == 'true'

        raw = self.__analysis.views_boxplot(not data)
        if data:
            return jsonify(dict(array=raw.to_dict('records')))
        else:
            return send_file("temp/image.png", mimetype='image/png', as_attachment=False)

class BoxRateView(MethodView):
    def __init__(
        self
    ) -> None:
        super().__init__()
        self.__analysis = AnalysisEngine(DataRepo(getenv('SQL_URL')))

    def get(self):

        data = request.args.get('data', 'true') == 'true'

        raw = self.__analysis.conv_rate_boxplot(not data)
        if data:
            return jsonify(dict(array=raw.to_dict('records')))
        else:
            return send_file("temp/image.png", mimetype='image/png', as_attachment=False)

class CoversionCountView(MethodView):
    def __init__(
        self
    ) -> None:
        super().__init__() 
        self.__analysis = AnalysisEngine(DataRepo(getenv('SQL_URL')))

    def get(self):

        data = request.args.get('data', 'true') == 'true'

        raw = self.__analysis.conversions_by_channel(not data)
        if data:
            return jsonify(dict(array=raw.to_dict('records')))
        else:
            return send_file("temp/image.png", mimetype='image/png', as_attachment=False)

class CoversionMonthView(MethodView):
    def __init__(
        self
    ) -> None:
        super().__init__() 
        self.__analysis = AnalysisEngine(DataRepo(getenv('SQL_URL')))

    def get(self):

        raw = self.__analysis.conversions_by_month()
        return jsonify(dict(array=raw.to_dict('records')))

class CoversionWeekView(MethodView):
    def __init__(
        self
    ) -> None:
        super().__init__() 
        self.__analysis = AnalysisEngine(DataRepo(getenv('SQL_URL')))

    def get(self):

        raw = self.__analysis.conversions_by_week()
        return jsonify(dict(array=raw.to_dict('records')))

class CoversionProductView(MethodView):
    def __init__(
        self
    ) -> None:
        super().__init__() 
        self.__analysis = AnalysisEngine(DataRepo(getenv('SQL_URL')))

    def get(self):

        raw = self.__analysis.conversions_by_product()
        return jsonify(dict(array=raw.to_dict('records')))
