import sqlite3
import functools

from flask import Blueprint,current_app, g,request,session,redirect,url_for,render_template

bp=Blueprint('yaminabe', __name__, url_prefix='/yaminabe')

@bp.route('/register', methods=['GET,POST'])
def yaminabe_register():
    db = get_db()
    error = None
    if request.method == 'POST':
        yaminabe_name = request.form['yaminabe']
        yaminabe=db.execute(
            'SELECT * FROM yaminabe WHERE yaminabe_name = ? ', (yaminabe_name, )
        ).fetchone()
        if yaminabe is not None:
            error = f'Yaminabe {yaminabe_name} is already registered.'
        else:
            db.execute(
                'INSERT INTO yaminabe (yaminabe_name) VALUES (?)',
                (yaminabe_name,)
            )
            db.commit()
            return redirect('/login')

    return render_template('/yaminabe/register.html', error=error)

@bp.route('/login', methods=['GET','POST'])
def yaminabe_login():
    db = get_db()
    error = None
    if request.method == 'POST':
        yaminabe_name = request.form['yaminabe']
        yaminabe=db.execute(
            'SELECT * FROM yaminabe WHERE yaminabe_name = ? ', (yaminabe_name, )
        ).fetchone()
        if yaminabe is None:
            error = 'Incorrect yaminabe name.'
        else :
            session['yaminabe_id'] = yaminabe['id']
            return redirect('/aa.html')

    return render_template('/yaminabe/login.html', error=error)

def yaminabe_logout():
    session.clear()
    return redirect('/aa.html')

def yaminabe_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('yaminabe.yaminabe_login'))
        return view(**kwargs)
    return wrapped_view
