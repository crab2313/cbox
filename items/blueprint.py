from flask import Blueprint, render_template, url_for
from models import Comic
from app import db


items = Blueprint('items', __name__, template_folder='templates')

@items.route('/')
def index():
    return render_template('index.html')