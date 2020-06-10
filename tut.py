from flask import Flask, redirect, url_for, render_template, request, session, flash 
import random 

from datetime import timedelta






app = Flask(__name__)

app.secret_key = "something" 

app.permanent_session_lifetime = timedelta (minutes = 10)  

@app.route("/login/", methods = ["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form ["nm"]
		if user.lower() in ["roxana", "josue", "mimy", "alex", "indya", "sombra"]:
			session["user"] = user.capitalize()
			
			return redirect(url_for("user"))
		else:

			return render_template ("login.html", Denied = "Invalid: Try Again!")

	else:
		if "user" in session: 
			flash ("Already Logged In!", "info")
			return redirect (url_for("user"))
		return render_template("login.html", Denied = "")


@app.route("/user")
def user():
	if "user" in session: 
		user = session["user"]
		#flash login used to be here
		return render_template ("index1.html", content = user, image = "wallhaven-nzlymy")
	else: 
		flash ("You are not logged in!", "info")
		return redirect (url_for("login"))


@app.route("/logout")
def logout ():
		session.pop ("user", None)
		flash ("You have been logged out", "info" )
		return redirect (url_for ("login"))

@app.route("/lob", methods = ["POST", "GET"])
def lob():
	if request.method == "POST":
		if request.form.get ('Logout') == 'Logout':
			
			session.pop ("user", None)
			return redirect(url_for ("login"))


#@app.route("/Roxana/")
#def user():
#	return render_template ("index1.html", content = "HMM!")

# Not necessary atm
#@app.route("/<name>") 
#def user(name):
#	return f"Hello {name}!"


@app.route ("/")
def home():
	return render_template ("index1.html", content = "[BLANK]")


@app.route("/admin/")
def admin(): 
	return redirect(url_for ("user")) 

@app.route ("/img", methods = ["POST", "GET"])
def img():
	img_list = ["wallhaven-nzlymy", "wallhaven-83kk62", "iceland for html", "icelandp2"]
	if request.method == "POST":
		if request.form.get ('Image') == 'Image':
			img = random.choice (img_list)
			return redirect (url_for ("user", image = img)) 
	else: 
		return redirect (url_for("user"))


@app.route ("/spain")
def spain(): 
	if "user" in session: 
		flash ("Welcome!", "info")
		return render_template("spain.html")
	else: 
		flash ("You are not logged in!", "info")
		return redirect (url_for ("login")) 

if __name__ == "__main__":
	app.run(debug = True)


			



