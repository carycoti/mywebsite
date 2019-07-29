from flask import Blueprint
from mywebsite import db
ac = Blueprint('ac',__name__)


@ac.route('/login')
def login():
    return 'Login'