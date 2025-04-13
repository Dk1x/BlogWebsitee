from django.contrib import admin
from .models import User, Post, Comment, Category

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'username', 'email', 'password')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'date_published')
    raw_id_fields = ('category',)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'date_posted')
    raw_id_fields = ('user',)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)