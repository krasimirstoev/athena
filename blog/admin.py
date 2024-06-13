from django.contrib import admin
from .models import Post, Category, SiteSettings, Comment, Page

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'category', 'post_time')
    search_fields = ('title', 'body')

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'category', 'post_time')
    search_fields = ('title', 'body')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'slug')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('blog_name', 'blog_subtitle', 'posts_per_page')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Page, PageAdmin)
