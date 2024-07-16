from db import db

def guardar_historia_clinica(datos):
    db['historia'].insert_one(datos)

def get_historias():
    historias = list(db['historia'].find())
    return historias