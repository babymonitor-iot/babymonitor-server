import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

try:
    os.remove("appBabyMonitor.db")
except Exception:
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///appBabyMonitor.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from .model.db_model import BabyMonitorSend, BabyMonitorReceive
from .controllers import main_controller

db.create_all()


