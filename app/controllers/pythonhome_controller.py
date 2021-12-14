from app.controllers.controller import ControllerBase
from flask import render_template


class HomeController(ControllerBase):
    @staticmethod
    def get():
        return render_template('pythonHome.html')