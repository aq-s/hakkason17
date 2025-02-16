from flask import Flask, render_template, request, jsonify
import json
import sqlite3
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# タグを受け取るエンドポイント
@app.route('/receive_tags/', methods=['POST'])
def receive_tags():
    try:
        # フロントエンドからのデータを取得
        data = request.json
        tags = data.get("tags")

        # データをリスト型に変換
        tags_list = list(tags)  # setやdict_keysなどもリスト化可能
        ingredients = tags_list
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400
        
        
    #APIキーの設定
    api_key = os.getenv('API_KEY') 
    client = genai.Client(api_key=api_key)


        # 食材を英語に変換
    def translate_ingredients(ingredients):
        response = client.models.translate_text(
        model='translate-text-1.0',
        text=ingredients,
        source='ja',
        target='en'
    )



    # 質問内容　後で食材のところは変数に変更
    response = client.models.generate_images(
    model='imagen-3.0-generate-002',
    prompt="""Please make a image of a black pot with {ingredients}.""",
    config=types.GenerateImagesConfig(
        number_of_images= 1,
    )
)

    for generated_image in response.generated_images:
        image = Image.open(BytesIO(generated_image.image.image_bytes))
        image.show()

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
    user_id = 1
    ingredients = "ばなな、いちご、カレールー、唐辛子"
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