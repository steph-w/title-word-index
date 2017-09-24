from flask import Flask, render_template, request
import re
import string
import json
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
	query = request.form['say']
	url = "http://openlibrary.org/search.json?title=" + query
	r = requests.get(url)
	json_data = json.loads(r.text)

	query_no_punctuation = query.replace(string.punctuation, "")
	documents = [(re.split(query_no_punctuation.upper(), json_data["docs"][i]["title_suggest"].upper()), json_data["docs"][i]["text"][0] ) for i in range(len(json_data["docs"]))]
	return render_template('submit.html', documents= documents, query=query_no_punctuation.upper())

if __name__ == "__main__":
	app.run()