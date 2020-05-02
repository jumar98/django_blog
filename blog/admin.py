from django.contrib import admin
from blog.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'picture', 'created_on']
    list_filter = ('author',)
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
