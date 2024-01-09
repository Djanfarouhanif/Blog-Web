from django.contrib import admin

from .models import Author, Comment, Article, Response


admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Article)
admin.site.register(Response)