from flask import Flask, render_template, redirect, Response, request
from schema.LoginSchema import LoginSchema
from http import HTTPStatus
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return redirect("/login")


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/check_logged_in_user", methods=["POST"])
def check_login():
    data = request.form
    app.logger.info(data)
    try:
        loginSchema = LoginSchema().load(dict(data))
    except ValidationError as err:
        return Response(json.dumps({"message": err.message, "data": err.valid_data, "status": HTTPStatus.BAD_REQUEST}))
    return Response({"status": HTTPStatus.ACCEPTED})


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
