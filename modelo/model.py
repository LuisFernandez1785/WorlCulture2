from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from flask_login import UserMixin
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Usuario(UserMixin, db.Model):
    __tablename__ = 'Usuarios'
    IdUsuario = Column(Integer, primary_key=True)
    NombreCompleto = Column(String, nullable=False)
    Telefono = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    Contrasenia = Column(String, nullable=False)
    Sexo = Column(String, nullable=False)
    Tipo = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        usua = self.query.all()
        return usua
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        usu = self.consultaIndividual()
        db.session.delete(usu)
        db.session.commit()
    def consultaIndividual(self):
        usu = self.query.get(self.IdUsuario)
        return usu
    @property
    def password(self):
        raise AttributeError('El atributo password no es de lectura')
    def validarPassword(self, Contrasenia):
        pwd = self.query.filter_by(Contrasenia=Contrasenia).first()
        print(Contrasenia)
        return pwd
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.IdUsuario
    def validar(self, Email, Contrasenia):
        user = Usuario.query.filter_by(Email=Email).first()
        if user != None:
            if user.validarPassword(Contrasenia):
                return user
        else:
            return None
