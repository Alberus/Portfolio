from flask import Flask
from multiprocessing import Process
from extentions import database
from extentions import api
from blueprints.pages import bp
from models.controles import ct
from models.tables import create_tables
from codes.telegram_bot import run_bot
#from models.pop_database import registrar

app = Flask(__name__)
app.config.from_object('config')
database.init_app(app)
api.init_app(app)
create_tables(app)
app.register_blueprint(bp)
app.register_blueprint(ct)


# Código usado para popular o banco de dados a partir do excel
""" with app.app_context():
    registrar() """

if __name__ == '__main__':
    p = Process(target=run_bot)
    p.start()
    app.run()




