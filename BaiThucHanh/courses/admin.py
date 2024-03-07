from django.contrib import admin
from courses.models import Category, Courses
from django.utils.html import mark_safe

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['name', 'description']
    list_filter = ['id', 'name', 'created_date']
    readonly_fields = ['my_image']

    def my_image(self, course):
        if course.image:
            return mark_safe(f"<img width='200' src='/static/{course.image.name}' />")

admin.site.register(Category)
admin.site.register(Courses, CourseAdmin)

# Register your models here.
