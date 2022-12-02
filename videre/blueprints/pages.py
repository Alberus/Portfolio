from flask import Blueprint, render_template

bp = Blueprint('blueprints', __name__, template_folder='templates')


@bp.route("/")
def index():
    return render_template('index.html')

@bp.route("/historiarum")
def outra():
    return render_template('historiarum.html')