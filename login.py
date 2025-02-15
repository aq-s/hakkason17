import sqlite3
import functools
from flask import Blueprint,current_app, g,request,session,redirect,url_for,render_template
from dp import *
from werkzeug.security import check_password_hash, generate_password_hash

bp_user =Blueprint('user', __name__, url_prefix='/user')


@bp_user.route('/login', methods=['POST'])
def login():
    db = get_db()
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = db.cursor()
        cur.execute(
            'SELECT * FROM user WHERE username = ? ', (username, )
        )
        user = cur.fetchone()
        if user is None or not(check_password_hash(user['password'], password)):
            error = 'Incorrect username or password.'
        else :
            session['user_id'] = user['id']
            return redirect(url_for('index'))

    return render_template('login.html', error=error)

@bp_user.route('/register', methods=['POST'])
def register():
    db = get_db()
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = db.cursor()
        cur.execute(
            'SELECT * FROM user WHERE username = ? ', (username, )
        )
        user = cur.fetchone()
        if user is not None:
            error = 'User {} is already registered.'.format(username)
        else:
            cur.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('user.login'))

    return render_template('register.html', error=error)

@bp_user.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view