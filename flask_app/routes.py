# Author: Prof. MM Ghassemi <ghassem3@msu.edu>
from flask import current_app as app, render_template

@app.route('/')
def hello():
	return render_template('index.html')