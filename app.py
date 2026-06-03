from flask import Flask, render_template, request
from core.shopee import get_products

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    products = None
    if request.method == "POST":
        keyword = request.form.get("keyword")
        page = request.form.get("page", 1)
        limit = request.form.get("limit", 20)
        if keyword:
            products = get_products(keyword=keyword, page=page, limit=limit)
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
