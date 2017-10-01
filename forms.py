from wtforms import StringField
from wtforms.fields import SubmitField
from wtforms.validators import DataRequired
from flask_wtf import Form

class SearchForm(Form):
	search = StringField('search', [DataRequired()])
	submit = SubmitField('Search', render_kw={'class': 'btn btn-success btn-block'})