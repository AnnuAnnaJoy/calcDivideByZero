from app.controllers.controller import ControllerBase
from flask import render_template


class AboutController(ControllerBase):
    @staticmethod
    def get():
        return render_template('about.html')