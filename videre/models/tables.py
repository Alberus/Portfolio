from extentions.database import db
import sqlalchemy as sa



class Estudante(db.Model):
    __tablename__ = "alunos"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome = sa.Column(sa.String(50))
    sexo = sa.Column(sa.String(1)) # F ou M
    turma = sa.Column(sa.String(2)) # Exemplo: 6A
    nt1 = sa.Column(sa.Integer)
    nt2 = sa.Column(sa.Integer)
    nt3 = sa.Column(sa.Integer)
    nt4 = sa.Column(sa.Integer)

    def __init__(self, nome, sexo, turma, nt1=0, nt2 = 0, nt3 = 0, nt4 = 0):
        self.nome = nome
        self.sexo = sexo
        self.turma = turma
        self.nt1 = nt1
        self.nt2 = nt2
        self.nt3 = nt3
        self.nt4 = nt4

    def __repr__(self):
        return '<Estudante %r>' % self.id

def create_tables(app, db=db):
    with app.app_context():
        db.create_all()











