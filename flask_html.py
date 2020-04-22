from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)
@app.route("/")
def home():
	#return render_template("index.html")
	return render_template("index.html")

@app.route("/Digital Signing")
def digital_signing():
	return render_template("digital_signing.html")

#@app.route('/')

if __name__ == "__main__":
	app.run(debug=True)



'''
app = Flask(__name__)
@app.route("/")
def home():
	#return render_template("index.html")
	return "Hello"

@app.route("/sal")
def function_sal():
	return "Hello sal"

if __name__ == "__main__":
	app.run(debug=True)

	'''