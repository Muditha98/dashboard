from __future__ import absolute_import
from app.mktcore.imports import *
from app.mktcore.admin import admin
from .forms import *
from .models import *

registerCRUD(admin, '/teacher', 'Teacher', FRM_TEACHER, MKT_TEACHER)