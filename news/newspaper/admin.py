from django.contrib import admin, sites
from .models import Post, Category, Comment, Author

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Author)

# Register your models here.
