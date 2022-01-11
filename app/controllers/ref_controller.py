from app.controllers.controller import ControllerBase
from flask import render_template


class RefController(ControllerBase):
    @staticmethod
    def get():
        return render_template('reference.html')