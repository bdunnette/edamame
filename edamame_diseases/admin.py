from django.contrib import admin
from categories.admin import CategoryBaseAdmin
from edamame_diseases.models import Disease

class DiseaseAdmin(CategoryBaseAdmin):
    pass

admin.site.register(Disease, DiseaseAdmin)