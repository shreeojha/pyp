from flask import Flask
app=Flask(__name__)
@app.route('/')
def webout():
	return '<h1>DevOps is fun.</h1>'

@app.route('/greet')
def greet():
	return '<h1>New feature is great</h1>'
app.run(host='0.0.0.0',port=7000)
