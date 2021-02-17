
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./relationship1.db'
db = SQLAlchemy(app)

class FactEmpleado(db.Model):
    __tablename__ = 'empleados'
    idEmpleado = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer)
    nombres = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    fechaNacimiento = db.Column(db.String(20))
    cargo = db.Column(db.String(20))
    email = db.Column(db.String(20))
    isActive = db.Column(db.Integer)
    experience = db.relationship('FactExperiencia',backref="empleado")

class FactExperiencia(db.Model):
    __tablename__ = 'experiencia'
    idExperiencia = db.Column(db.Integer, primary_key=True)
    idEmpleado = db.Column(db.Integer, db.ForeignKey('empleados.idEmpleado')) 
    empresa = db.Column(db.String(20))  
    cargo = db.Column(db.String(20))    
    isActive = db.Column(db.Integer)