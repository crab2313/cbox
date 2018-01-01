from app import app, db

import models
import views
from items.blueprint import items

app.register_blueprint(items, url_prefix='/items')

if __name__ == '__main__':
    app.run(debug=True)