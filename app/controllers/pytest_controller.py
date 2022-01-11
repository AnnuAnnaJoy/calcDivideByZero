from app.controllers.controller import ControllerBase
from flask import render_template


class PytestController(ControllerBase):
    @staticmethod
    def get():
        return render_template('pytest.html')