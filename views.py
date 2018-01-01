from flask import render_template
from app import app

def new_item(title, image):
    class Item:
        def __init__(self, title, image):
            self.title = title
            self.image = image
    return Item(title, image)

test_items = [new_item('hello', 'world'), new_item('foo', 'bar')]

@app.route('/')
def homepage():
    return render_template('homepage.html')