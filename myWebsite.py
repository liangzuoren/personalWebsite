from flask import Flask, render_template, url_for, send_from_directory
from flask_flatpages import FlatPages
import os

#setting up Flatpages
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

#Setting up Flask
app = Flask(__name__)
flatpages = FlatPages(app)
app.config.from_object(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/contactme')
def contact():
	return render_template('contactme.html')

#Grab all posts in the flatpages path to display on the posts page
@app.route('/posts/')
def posts():
	posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
	posts.sort(key=lambda item:item['date'], reverse = False)	
	return render_template('posts.html', posts=posts)
	
@app.route('/post/<name>/')
def post(name):
	path = '{}/{}'.format(POST_DIR,name)
	post = flatpages.get_or_404(path)
	return render_template('post.html', post=post)

@app.route('/contact/resume/')
def resume():
	workingdir = os.path.abspath(os.getcwd())
	filepath = workingdir + '/static/files/'
	return send_from_directory(filepath,'Resume2021Data.pdf')
	
if __name__ == '__main__':
	app.run(debug=True)
