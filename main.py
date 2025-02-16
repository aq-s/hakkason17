from flask import Flask, render_template, request, jsonify
import json
import sqlite3
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

app = Flask(__name__)

ingredients = ["ばなな", "いちご", "カレールー", "唐辛子", "USB"]

#APIキーの設定
client = genai.Client(api_key="GEMINI_API_KEY")


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