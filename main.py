from flask import Flask, render_template, request, jsonify
import json
import sqlite3

app = Flask(__name__)

# データベースに接続する関数
def get_db_connection():
    conn = sqlite3.connect('BlackFoods.db')
    conn.row_factory = sqlite3.Row
    return conn

#　登録・出力エンドポイント
@app.route('/add_BlackFoods/', methods=['POST'])

#フロント側に送るデータ（出力）
def send_BlackFoods():
    photo = 0 #ここはgeminiの出力の内容を入れる予定
    return render_template('main.html', photo=photo)


#登録
def add_BlackFoods():
    
    food_data = request.form #ここはフロント班次第で変更
    photo = photo #ここはgeminiの接続ごとに変える
    
    # 各データの取得(foods_idは自動採番)
    user_id = user_id
    ingredients = food_data['ingredients']
    photo = photo
    
    # 画像をバイナリデータに変換
    photo_data = photo.read()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    
    cursor.execute('''
        INSERT INTO foods (foods_id, user_id, ingredients, photo)
        VALUES (?, ?, ?, ?)
    ''', (user_id, ingredients, photo_data))

    conn.commit()
    conn.close()
    
    return jsonify({"message": "登録されました！"})
    