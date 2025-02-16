import google.generativeai as genai

api_key = "API_KEY"
genai.configure(api_key=api_key)

try:
    models = genai.list_models()
    print("API接続成功！利用可能なモデル一覧：", models)
except Exception as e:
    print("API接続エラー:", e)
