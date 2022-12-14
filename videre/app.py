from flask import Flask

from extentions import database
from blueprints.pages import bp
from models.controles import ct
from models.tables import create_tables

app = Flask(__name__)
app.config.from_object('config')
database.init_app(app)
create_tables(app)
app.register_blueprint(bp)
app.register_blueprint(ct)






if __name__ == "__main__":
    app.run()





