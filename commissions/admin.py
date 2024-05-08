from django.contrib import admin

from .models import Commission, Job, JobApplication


class JobInline(admin.TabularInline):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [JobInline]


class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication


admin.site.register(Commission, CommissionAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
