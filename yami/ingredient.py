import sqlite3

import click
from flask import Blueprint,current_app, g,request,session,redirect,url_for,render_template
#login.pyからget_db関数をimportする
from db import get_db

bp=Blueprint('ingredient', __name__, url_prefix='/ingredient')

YAMINABE_CAPACITY = 5
#材料をデータベースに登録する
@bp.route('/add', methods=['POST'])
#@login_required
def add():
    db = get_db()
    error = None
    if request.method == 'POST':
        ingredient_name = request.form['ingredient']
        yaminabe_id = session['yaminabe_id']
        db.execute(
            'INSERT INTO ingredient (ingredient_name,yaminabe_id) VALUES (?)', (ingredient_name,yaminabe_id)
        )
        db.commit()
        #あるyaminabeに登録されている材料の数を確認する
        ingredient_counts = db.execute(
            'SELECT COUNT(*) FROM ingredient WHERE yaminabe_id = ?', (yaminabe_id,)
        ).fetchone()[0]
        if ingredient_counts >= YAMINABE_CAPACITY:
            return redirect('/hogehoge')
        else:
            return render_template('next.html')

    return render_template('add.html', error=error)