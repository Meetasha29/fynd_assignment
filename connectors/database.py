from flask import current_app
from flask_sqlalchemy import SQLAlchemy as SQLAlchemyBase

db = SQLAlchemyBase(current_app)
