from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
    return render_template("index.html")

@app.route("/home", methods=["GET","POST"])
def home_page():
    return render_template("home.html")

## 実行
if __name__ == "__main__":
    app.run(debug=True)