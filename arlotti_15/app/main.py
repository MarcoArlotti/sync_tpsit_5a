# app/main.py
from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for,jsonify
)
from app.db import post_db, get_db

bp = Blueprint('main', __name__)

# pagina principale
@bp.route('/')
def index():
    return render_template("cerca_localita.html")


# endpoint AJAX
@bp.route('/cerca')
def cerca():
    query = request.args.get("q", "")

    rows = prendi_localita(query)

    return jsonify([dict(r) for r in rows])


# esempio funzione DB (la tua va bene, questa è demo)
def prendi_localita(ricerca):
    db = get_db()

    if not ricerca:
        return []

    query = """
        SELECT *
        FROM comuni
        WHERE name LIKE ?
    """

    rows = db.execute(query, ('%' + ricerca + '%',)).fetchall()
    return [dict(r) for r in rows]


if __name__ == "__main__":
  app.run(debug=True)