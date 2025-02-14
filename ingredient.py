import sqlite3

import click
from flask import Blueprint,current_app, g,request,session,redirect,url_for,render_template
from login import get_db
from werkzeug.security import check_password_hash, generate_password_hash

bp_ing=Blueprint('ingredient', __name__, url_prefix='/ingredient')

@bp_ing.route('/add', methods=['POST'])
def add():
    db = get_db()
    error = None
    if request.method == 'POST':
        ingredient_name = request.form['ingredient_name']
        cur = db.cursor()
        cur.execute(
            'INSERT INTO ingredient (ingredient_name,user_id) VALUES (?)', (ingredient_name,session['user_id'] )
        )
        db.commit()
        return redirect(url_for('index'))

    return render_template('add.html', error=error)