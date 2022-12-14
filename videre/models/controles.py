from flask import Blueprint, request, url_for, redirect, render_template
from models.tables import Estudante
from extentions.database import db

ct = Blueprint('controlador', __name__, template_folder='models')


@ct.route("/cadastrar_estudante", methods=['POST', 'GET'])
def cad_estudante():
    if request.method == "POST":
        nome = request.form["nome"]
        sexo = request.form["sexo"]
        turma = request.form["turma"]
        e = Estudante(nome, sexo, turma)
        db.session.add(e)
        db.session.commit()
        return redirect("/estudantes")
    return render_template('cadastrar_estudante.html')

@ct.route("/delete/<int:id>")
def delete(id):
  del_estud = Estudante.query.filter_by(id=id).first()
  db.session.delete(del_estud)
  db.session.commit()
  return redirect("/estudantes")

@ct.route("/update_estudante/<int:id>", methods=['GET','POST'])
def update_estudante(id):
  if request.method == 'POST':
    to_update = Estudante.query.filter_by(id=id).first()
    nome = request.form['nome']
    sexo = request.form['sexo']
    turma = request.form['turma']
    nt1 = request.form['nt1']
    nt2 = request.form['nt2']
    nt3 = request.form['nt3']
    nt4 = request.form['nt4']
    e = Estudante(nome, sexo, turma)
    to_update.nome = nome
    to_update.sexo = sexo
    to_update.turma = turma
    to_update.nt1 = nt1
    to_update.nt2 = nt2
    to_update.nt3 = nt3
    to_update.nt4 = nt4
    db.session.commit()
    return redirect("/estudantes")
  to_update = Estudante.query.filter_by(id=id).first()
  return render_template("update_estudante.html", update_estudante=to_update)

@ct.route("/estudantes")
def lista_estudantes():
  lista_estudantes = Estudante.query.all()
  return render_template('lista_estudantes.html', estuds=lista_estudantes)

# from extentions.database import db
# from models.tables import Estudante

# class Estudantes_CRUD:
#   def select(self):
#     with db:
#       data = db.session.query(Estudante).all()
#       return data
  
#   def insert(self, nome, sexo, turma):
#     with db:
#       e = Estudante(nome=nome, sexo=sexo, turma=turma)
#       db.session.add(e)
#       db.session.commit()

#   def update(self, nome, turma):
#     with db:
#       db.session.query(Estudante).filter(Estudante.nome == nome).update({"turma": turma})
#       db.session.commit()

#   def delete(self, nome):
#     with db:
#       db.session.query(Estudante).filter(Estudante.nome == nome).delete()
#       db.session.commit()







