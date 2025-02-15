import sqlite3

import click
from flask import Blueprint,current_app, g,request,session,redirect,url_for,render_template
from login import get_db,login_required
from werkzeug.security import check_password_hash, generate_password_hash

bp_ing=Blueprint('ingredient', __name__, url_prefix='/ingredient')

YAMINABE_CAPACITY = 5
#材料をデータベースに登録する
@bp_ing.route('/add', methods=['POST'])
@login_required
def add():
    db = get_db()
    error = None
    if request.method == 'POST':
        ingredient_name = request.form['ingredient_name']
        max_id = db.execute('SELECT MAX(yaminabe_id) FROM ingredient').fetchone()[0]
        if max_id is None:
            yaminabe_id = 0
        else:
            max_id_counts=db.execute('SELECT COUNT(yaminabe_id) FROM ingredient WHERE yaminabe_id = ?', (max_id,)).fetchone()[0]
            if max_id_counts >= YAMINABE_CAPACITY:
                yaminabe_id = max_id+1
            else:
                yaminabe_id = max_id

        cur.execute(
            'SELECT * FROM ingredient WHERE ingredient_name = ? ', (ingredient_name, )
        )
        cur = db.cursor()
        cur.execute(
            'INSERT INTO ingredient (ingredient_name,user_id,yaminabe_id) VALUES (?)', (ingredient_name,session['user_id'] ,yaminabe_id)
        )
        db.commit()
        return redirect(url_for('index'))

    return render_template('add.html', error=error)