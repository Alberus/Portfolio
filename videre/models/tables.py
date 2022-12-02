from videre import db


class Turma(db.Model):
    __tablename__ = "turmas"
    id = db.Column(db.Integer, primary_key=True)
    turma = db.Column(db.String(2), unique=True) # Exemplo: 6A

    def __init__(self, turma):
        self.turma = turma

    def __repr__(self):
        return '<Turma %r>' % self.turma


class Estudante(db.Model):
    __tablename__ = "alunos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    sexo = db.Column(db.String(1)) # F ou M
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'))

    estudante = db.relationship('Turma', foreign_keys=turma_id)

    def __init__(self, nome, sexo, turma_id):
        self.nome = nome
        self.sexo = sexo
        self.turma_id = turma_id

    def __repr__(self):
        return '<Estudante %r>' % self.id



