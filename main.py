from flask import Flask, render_template, request, session
import re
import string
import json
import requests
from forms import SearchForm
from flask_wtf import csrf
from flask_wtf.csrf import CsrfProtect
app = Flask(__name__)
c = CsrfProtect(app)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
	form = SearchForm()
	if form.validate_on_submit():
		print "Form Validated"
		csrf.generate_csrf()
		query = form.search.data
		url = "http://openlibrary.org/search.json?title=" + query
		r = requests.get(url)
		json_data = json.loads(r.text)
		query_no_punctuation = query.replace(string.punctuation, "")
		documents = [(re.split(query_no_punctuation.upper(), json_data["docs"][i]["title_suggest"].upper()), json_data["docs"][i]["text"][0] ) for i in range(len(json_data["docs"]))]
		return render_template('derived.html', documents= documents, query=query_no_punctuation.upper(), form=form)
	return render_template('search.html', form=form)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == "__main__":
	app.run()