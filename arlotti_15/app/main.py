# app/main.py
from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from app.db import post_db, get_db

bp = Blueprint('main', __name__)

def prendi_localita():
  db = get_db()
  query = """
        SELECT *
        FROM comuni;
    """
  comuni = db.execute(query).fetchall()
  return [dict(comune) for comune in comuni]


@bp.route('/')
def index():
  localita = prendi_localita()
  return render_template('cerca_localita.html', localita=localita)
