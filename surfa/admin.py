from django.contrib import admin
from .models import Post_Projects
# Register your models here.

class Post_ProjectsAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'slug', 'status','url')
    list_filter = ("status",)
    search_fields = ['title', 'url']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post_Projects, Post_ProjectsAdmin)
