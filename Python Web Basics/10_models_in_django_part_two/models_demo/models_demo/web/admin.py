from django.contrib import admin

from models_demo.web.models import Employee, \
    NullBlankDemo, Department, Project, Category


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'level')
    list_filter = ('level',)
    fieldsets = (
        ('Short Info',
         {'fields': ('first_name', 'last_name', 'email')}),
        ('Personal info',
         {'fields': ('level', 'years_of_experience', 'years_of_experience2', 'review', 'department')}),
        ('Company info',
         {'fields': ('is_full_time', 'projects', 'start_date')}),
         )




@admin.register(NullBlankDemo)
class NullBlankAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
