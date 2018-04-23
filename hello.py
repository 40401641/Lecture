from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def defult():
	return ("Hello")

@app.route('/hello/<name>')
def hello(name=None):
	user = {'name':name}
	return render_template('hello.html',user=user)

@app.route('/hello/<name>')
def hello(name=None):
	return render_template('conditional.html', name=name)

@app.route('/users/')
def users():
	names = ['simon','thomas','lee','jamie','sylvester']
	return render_template('loops.html', names=names)

if __name__=="__main__":
	app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug= True)