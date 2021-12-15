"""A simple flask web app"""
from flask import Flask

from app.controllers.aaa_controller import AAAcontroller
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.history_controller import HistoryController
from app.controllers.oop_controller import OOPcontroller
from app.controllers.pylint_controller import PylintController
from app.controllers.solid_controller import SolidController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/history", methods=['GET'])
def history_get():
    return HistoryController.get()

@app.route("/pylint", methods=['GET'])
def pylint_page_get():
    return PylintController.get()

@app.route("/oop", methods=['GET'])
def oop_page_get():
    return OOPcontroller.get()

@app.route("/aaa", methods=['GET'])
def aaa_page_get():
    return AAAcontroller.get()

@app.route("/solid", methods=['GET'])
def solid_page_get():
    return SolidController.get()