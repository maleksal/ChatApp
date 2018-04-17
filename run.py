from flask import Flask, render_template,url_for,redirect,request
from app import *
app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
	if request.method == "POST":
		Data = Database(request.form["User"],request.form["msg"])
		store = Store(Data)
		return render_template("app.html",message=store.getall())
	return render_template("app.html",mesg=["No Message Yet..."])

if __name__ == '__main__':
	app.run()