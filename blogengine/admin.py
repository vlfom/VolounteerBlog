import models
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

class TagAndCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(models.UserProfile)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, TagAndCategoryAdmin)
admin.site.register(models.Tag, TagAndCategoryAdmin)