from app.controllers.controller import ControllerBase
from flask import render_template

class AAAcontroller(ControllerBase):
    @staticmethod
    def get():
        return render_template('aaa.html')