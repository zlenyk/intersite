from django.contrib import admin
from interviews.models import Interview,Tag,Comment,Category

admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Interview)
admin.site.register(Category)
