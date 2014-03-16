from django.contrib import admin

.models import NotebookReport, NotebookReportee, NotebookReportTimes


class ReportTimeInline(admin.TabularInline):
    model = NotebookReportTimes


class ReporteeInline(admin.TabularInline):
    model = NotebookReportee


class NotebookReportAdmin(admin.ModelAdmin):
    model = NotebookReport
    inlines = [
        ReporteeInline,
        ReportTimeInline
    ]

admin.site.register(NotebookReport, NotebookReportAdmin)
