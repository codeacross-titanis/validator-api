from django.contrib import admin

from .models import Badge, Student


class BadgeInline(admin.TabularInline):
    model = Badge
    fields = ('name', 'is_validated', 'validated_by', 'validated_at', 'completed_date')


class StudentAdmin(admin.ModelAdmin):
    inlines = [BadgeInline]

admin.site.register(Badge)
admin.site.register(Student, StudentAdmin)
