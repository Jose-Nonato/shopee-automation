from flask import Flask, render_template
from core.shopee import get_products

app = Flask(__name__)

@app.route("/")
def hello_world():
    resp = get_products()
    return render_template("index.html", resp=resp)

if __name__ == "__main__":
    app.run(debug=True)
