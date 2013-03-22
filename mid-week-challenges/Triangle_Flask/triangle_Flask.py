# This is whre you can start you python file for your week1 web app
# Name: Anthony Leonardi

import flask, flask.views
import os
app = flask.Flask(__name__)

app.secret_key = "bacon"


def is_triangle(x,y,z):
	if (((x+y)>z) and ((y+z)>x) and ((z+x)>y)):
		return "Yes"
	else:
		return "No"

class View(flask.views.MethodView):


	def get(self):
		return flask.render_template('index.html')

	def post(self):
		#result = eval(flask.request.form['expression'])
		a = float(flask.request.form['a'])
		b = float(flask.request.form['b'])
		c = float(flask.request.form['c'])
		result = is_triangle(a,b,c)
		sides = "side lengths: " + str(a) + " : " + str(b) + " : " + str(c)
		flask.flash(sides)
		flask.flash(result)
		return self.get()



app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
app.run()