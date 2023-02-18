# pylint: disable=no-member, import-error
from flask import Flask
from di.container import Container
from views.conversion_view import ConversionView
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
    test_view = TestView.as_view(name="test")

    app.add_url_rule(
        "/conversion/basic",
        view_func=conversion_view,
        methods=["GET"],
    )
    app.add_url_rule(
        "/hi",
        view_func=test_view,
        methods=["GET"],
    )
    return  app

container = Container()
app = create_app(container)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
