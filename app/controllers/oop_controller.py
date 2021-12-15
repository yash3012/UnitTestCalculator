from app.controllers.controller import ControllerBase
from flask import render_template

class OOPcontroller(ControllerBase):
    @staticmethod
    def get():
        return render_template('oop.html')