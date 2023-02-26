from flask import Blueprint, request, url_for, redirect, render_template
from flask_restful import Resource
from models.tables import Estudante, Usuario
from extentions.database import db
from extentions.api import api
import json
import requests

ct = Blueprint('controlador', __name__, template_folder='models')

#Cadastra estudantes na tabela alunos
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
#Exclui registro na tabela alunos
@ct.route("/delete/<int:id>")
def delete(id):
  del_estud = Estudante.query.filter_by(id=id).first()
  db.session.delete(del_estud)
  db.session.commit()
  return redirect("/estudantes")
#Altera registros na tabela alunos
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
#Lista dos os estudantes registrados na tabela alunos
@ct.route("/estudantes")
def lista_estudantes():
  lista_estudantes = Estudante.query.all()
  return render_template('lista_estudantes.html', estuds=lista_estudantes)


@ct.route("/users/", methods=['POST', 'PUT', 'GET', 'DELETE'])
def usuarios_adm():
  return render_template("users.html")

class Usuarios(Resource):

  def get(self, id):                #consulta nome de usuário
    user = Usuario.query.filter_by(id)
    try:
      response={
        'id':user.id,
        'nome':user.nome
      }
    except IndexError:
      mensagem = "Usuario de ID {} não existe".format(id)
      response = {"status":"erro", "mensagem":mensagem}
    except Exception:
      mensagem = "Erro Desconhecido"
      response = {"status":"erro", "mensagem":mensagem}
    return response

  def put(self, id):                #atualiza dados
    user = Usuario.query.filter_by(id)
    dados = request.json
    if "nome" in dados:
      user.nome = dados['nome']
    if "senha" in dados:
      user.senha = dados['senha']
    db.session.commit()
    response = {
      'id':user.id,
      'nome':user.nome,
      'senha':user.senha
    }
    return response

  def delete(self,id):            #deleta usuario
    user = Usuario.query.filter_by(id)
    mensagem = "Usuario {} excluido com sucesso".format(user.nome)
    db.session.delete(user)
    db.session.commit()
    return {"status":"sucesso", "mensagem":mensagem}
  


class ListaUsuarios(Resource):
  def post(self):
    dados = request.json
    nome = dados['nome']
    senha = dados['senha']
    user = Usuario(nome, senha)
    db.session.add(user)
    db.session.commit()
    return "Adicionado com sucesso"
  
  def get(self):
    users = Usuario.query.all()
    response = [{'id':i.id, 'nome':i.nome} for i in users]
    return response

api.add_resource(Usuarios, "/usuario/<int:id>/")
api.add_resource(ListaUsuarios, "/usuarios/")











