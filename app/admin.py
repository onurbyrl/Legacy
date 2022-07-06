from django.contrib import admin
from app.models import About, Project, Contact


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')