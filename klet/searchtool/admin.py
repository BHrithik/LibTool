from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *
from .resources import RecordResource


class ModelAdmin(ImportExportModelAdmin):
    resource_class = RecordResource
    list_display = ['authorKorean', 'authorEnglish', 'workTitle', 'genre', 'translator', 'sourceTitle', 'publisher', 'year', 'subjects', 'summary']
    search_fields = ['authorKorean', 'authorEnglish', 'workTitle', 'genre', 'translator', 'sourceTitle', 'publisher', 'year', 'yearCreated', 'authorEnglish2', 'uid2','subjects', 'summary']
    list_per_page = 20

admin.site.register(Record, ModelAdmin)