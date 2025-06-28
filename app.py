from flask import Flask, render_template, request
from scrapers.remoteok import scrape_remoteok  # ← 여기 변경

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    results = scrape_remoteok(keyword)  # ← 여기 변경
    return render_template("results.html", keyword=keyword, jobs=results)

if __name__ == "__main__":
    app.run(debug=True)
