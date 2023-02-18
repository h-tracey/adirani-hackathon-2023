# pylint: disable=no-member, import-error
from flask.views import MethodView

class TestView(MethodView):
    def __init__(
        self
    ) -> None:
        super().__init__()

    def get(self):
        return 'hi :)'