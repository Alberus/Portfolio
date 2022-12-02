from flask import Flask

from extentions import database
from blueprints.pages import bp

app = Flask(__name__)
app.config.from_object('config')
database.init_app(app)
app.register_blueprint(bp)





if __name__ == "__main__":
    app.run()





