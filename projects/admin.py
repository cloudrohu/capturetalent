from django.contrib import admin
from .models import OngoingProject, ProjectCategory

# Register your models here.

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(OngoingProject)
class OngoingProjectAdmin(admin.ModelAdmin):

    list_display = ['title', 'category', 'created_at']
    prepopulated_fields = {"slug": ("title",)}