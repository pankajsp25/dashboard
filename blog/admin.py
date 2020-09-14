from django.contrib import admin

# Register your models here.
from blog.models import BlogCategory, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_author_name', 'created_at', 'updated_at')

    def get_author_name(self, obj):
        return  obj.author.get_full_name()

    get_author_name.short_description = 'Author'

admin.site.register(BlogCategory)
admin.site.register(Blog, BlogAdmin)