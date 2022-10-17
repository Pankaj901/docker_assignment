# flask-app.py
from flask import Flask, request


# create a Flask instance
app = Flask(__name__)




				
# Routes refer to url'
# our root url '/' will show our html description
@app.route('/', methods=['GET'])
def hello_world():
    # return a html format string that is rendered in the browser
	return "hello world \n this is my task 3 in docker assignment"


  
if __name__ == "__main__":
	# for debugging locally
	# app.run(debug=True, host='0.0.0.0',port=5000)
	
	# for production
	app.run(host='0.0.0.0', port=5000)