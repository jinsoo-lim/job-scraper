from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ 서버 잘 작동 중입니다!"

if __name__ == "__main__":
    app.run(debug=True)
