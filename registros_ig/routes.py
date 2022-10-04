from flask import jsonify,render_tempalte

from registros_ig import app
from registros_ig.model import select_all

@app.route("/")
def index():

    return render_tempalte("index.html")

@app.route("/api/v1.0/all")
def all_movements():
    registro = select_all()
    return jsonify(registro)

@app.route("/api/v1.0/new", methods=["POST"])
def new():
    return "Esto hara un alta"

@app.route("/api/v1.0/delete/<int:id>", methods=["DELETE"])
def delete_id(id):
    return f"Esto Borrara {id}"

@app.route("/api/v1.0/update/<int:id>", methods=["PUT"])
def new(id):
    return f"Esto modificará {id}"

