from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for


class HistoryController(ControllerBase):
    @staticmethod
    def get():
        calculations = Calculator.get_calculations()
        return render_template('history.html',calculations=calculations)






