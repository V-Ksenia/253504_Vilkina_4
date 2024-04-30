from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Article)
admin.site.register(CompanyInfo)
admin.site.register(FAQ)
admin.site.register(Contact)
admin.site.register(Vacancy)
admin.site.register(Review)