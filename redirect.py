from flask import Flask, redirect, url_for, abort, request
app=Flask(__name__)

@app.route("/")
def root():
	return "The default, 'root' route"
@app.route("/hello/")
def hello():
	name=request.args.get('name','')
	if name=='':
		return "no param supplied"
	else:
		return "Hello %s" % name

@app.route("/private")
def private():
	return redirect(url_for('login'))

@app.route("/login")
def login():
	return "Now we would get username & password"

@app.route("/force404")
def force404():
	abort (404)

@app.errorhandler(404)
def page_not_found(error):
	return "Couldn't find the page you requested.",404

@app.route('/static-example/img')
def statci_example_img():
	start='<img src="'
	url=url_for('static', filename='SVT.jpg')
	end='">'
	return start+url+end, 200

@app.route("/account", methods=['GET','POST'])
def account():
	if request.method == 'POST':
		print(request.form)
		name = request.form['name']
		return "Hello %s" % name
	else:
		page='''
		<html><body>
		<form action="" method="post" name="form>"
			<label for="name">Name:</label>
			<input type="text" name="name" id="name"/>
			<input type="submit" name="submit" id="submit"/>
		</form>
		</body></html>'''
		return page

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
	return str(first+second)


if __name__ == "__main__":
	app.run(host= '0.0.0.0', debug = True)