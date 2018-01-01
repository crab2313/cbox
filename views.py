from flask import render_template, request, url_for, redirect
from app import app
from forms import UploadComicForm


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/import', methods=['GET', 'POST'])
def upload():
    form = UploadComicForm()
    if form.validate_on_submit():
        return render_template('homepage.html')
    return render_template('import.html', form=form)

@app.route('/collections')
def collections():
    return render_template('collections.html')