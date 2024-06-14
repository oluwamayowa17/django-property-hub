from django.contrib import admin

# Register your models here.
from AppTwo.models import UserProfile, Post, Comment, Category, Location, Property, Contact 

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(UserProfile)
admin.site.register(Property)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Contact)