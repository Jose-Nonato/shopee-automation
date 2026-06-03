from flask import Flask, render_template
from core.shopee import get_products
from database import users

app = Flask(__name__)

@app.route("/")
def hello_world():
    usuarios = list(users.find({}, {"_id": 0}))
    return render_template("index.html", resp=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
