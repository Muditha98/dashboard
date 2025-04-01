from __future__ import absolute_import
from app.mktcore.wtfimports import *
from app.mktcore.constants import len2
from .models import *
from flask_babel import lazy_gettext as _l

class FRM_TEACHER(exform):
    LastName = TextField(requiredlabel('Last Name', '*'), 
                        validators=[validators.Required(),
                                  validators.Regexp('^[A-Z][^\s]*$', message='Must start with capital letter and contain no whitespace'),
                                  validators.Length(max=30)])
    
    FirstName = TextField(requiredlabel('First Name', '*'), 
                         validators=[validators.Required(),
                                   validators.Regexp('^[A-Z][^\s]*$', message='Must start with capital letter and contain no whitespace'),
                                   validators.Length(max=30)])
    
    Gender = TextField(requiredlabel('Gender', '*'),
                      validators=[validators.Required(),
                                validators.Length(max=1)])
    
    Grade = TextField('Grade',
                     validators=[validators.Optional(),
                               validators.Regexp('^\d{1,2}$', message='Must be numeric'),
                               validators.Length(max=2)])
    
    Country = TextField(requiredlabel('Country', '*'),
                       validators=[validators.Required(),
                                 validators.Length(max=6)])
    
    Email = TextField('Email',
                     validators=[validators.Optional(),
                               validators.Email(),
                               validators.Length(max=50)])

    @staticmethod
    def setDisable():
        return ['Grade', 'Country']

    @staticmethod
    def setWidth():
        control_list = [('Gender', len2), ('Grade', len2)]
        return control_list