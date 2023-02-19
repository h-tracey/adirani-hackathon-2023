# pylint: disable=no-member, import-error
from flask import Flask
from di.container import Container
from views.conversion_views import (
    ConversionView,
    ScatterView,
    ScatterTypeView,
    BoxRateView,
    BoxViewsView,
    CoversionCountView,
    CoversionMonthView,
    CoversionProductView,
    CoversionWeekView
)
from views.touchpoint_views import TouchpointsCountView
from views.test_view import TestView


def create_app(container: Container) -> Flask:
    """create a flask application instance

    Args:
        container (Container): DI insight service container

    Returns:
        Flask: flask instance with defined endpoints
    """
    app = Flask("conversions_api")
    app.container = container
    
    conversion_view = ConversionView.as_view(name="conversion_view")
    scatter_view = ScatterView.as_view(name='scatter_view')
    scatter_type_view = ScatterTypeView.as_view(name='scatter_type_view')
    box_rate_view = BoxRateView.as_view(name='box_rate_view')
    box_view_view = BoxViewsView.as_view(name='box_view_view')
    test_view = TestView.as_view(name="test")
    conversion_count_view = CoversionCountView.as_view(name ='conversion_count_view')
    touchpont_count_view = TouchpointsCountView.as_view(name = 'touchpont_count_view')
    conversion_month = CoversionMonthView.as_view(name ='conversion_month')
    conversion_prod = CoversionProductView.as_view(name ='conversion_prod')
    conversion_week = CoversionWeekView.as_view(name ='conversion_week')
    
    
    app.add_url_rule("/conversion/count", view_func=conversion_count_view, methods=["GET"])
    app.add_url_rule("/conversion/month", view_func=conversion_month, methods=["GET"])
    app.add_url_rule("/conversion/week", view_func=conversion_week, methods=["GET"])
    app.add_url_rule("/conversion/product", view_func=conversion_prod, methods=["GET"])
    app.add_url_rule("/hi", view_func=test_view, methods=["GET"])
    app.add_url_rule("/scatter-views", view_func=scatter_view, methods=["GET"])
    app.add_url_rule("/scatter-type", view_func=scatter_type_view, methods=["GET"])
    app.add_url_rule("/box-views", view_func=box_rate_view, methods=["GET"])
    app.add_url_rule("/box-conversion", view_func=box_view_view, methods=["GET"])
    app.add_url_rule("/touchpoints", view_func=touchpont_count_view, methods=["GET"])
    return  app

container = Container()
app = create_app(container)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
