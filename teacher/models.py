from __future__ import absolute_import
from app.mktcore.mdlimports import *

class MKT_TEACHER(exmodel):
    ID = db.Column(db.String(3), primary_key=True)
    LastName = db.Column(db.String(30), nullable=False)
    FirstName = db.Column(db.String(30), nullable=False)
    Gender = db.Column(db.String(1), nullable=False, default='M')
    Grade = db.Column(db.String(2))
    Country = db.Column(db.String(6), nullable=False)
    Email = db.Column(db.String(50))

class MKT_TEACHER_INAU(exmodel):
    ID = db.Column(db.String(3), primary_key=True)
    LastName = db.Column(db.String(30), nullable=False)
    FirstName = db.Column(db.String(30), nullable=False)
    Gender = db.Column(db.String(1), nullable=False, default='M')
    Grade = db.Column(db.String(2))
    Country = db.Column(db.String(6), nullable=False)
    Email = db.Column(db.String(50))

class MKT_TEACHER_HIST(exmodel):
    ID = db.Column(db.String(3), primary_key=True)
    LastName = db.Column(db.String(30), nullable=False)
    FirstName = db.Column(db.String(30), nullable=False)
    Gender = db.Column(db.String(1), nullable=False, default='M')
    Grade = db.Column(db.String(2))
    Country = db.Column(db.String(6), nullable=False)
    Email = db.Column(db.String(50))