from extentions.database import db
from models.tables import Estudante
import pandas as pd


# Código usado para popular o banco de dados a partir do excel, contudo há um problema
# e está duplicando as inserções no banco de dados
""" alunos_df = pd.read_excel("D:\Educacional\Resumo.xlsx") #dataframe de alunos

def registrar():
    for i in range(0,208):
        _nome = alunos_df.loc[i, "Nome"].title()
        _sexo = alunos_df.loc[i, "Sexo"]
        _turma = alunos_df.loc[i, "Turma"]
        _nt1 = alunos_df.loc[i, "nt1"]
        _nt2 = alunos_df.loc[i, "nt2"]
        _nt3 = alunos_df.loc[i, "nt3"]
        _nt4 = alunos_df.loc[i, "nt4"]
        _e = Estudante(_nome, _sexo, _turma, _nt1, _nt2, _nt3, _nt4)
        db.session.add(_e)
    db.session.commit()
 """


