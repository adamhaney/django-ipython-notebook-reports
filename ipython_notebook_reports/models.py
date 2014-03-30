from django.db import models


class Notebook(models.Model):
    notebook = models.FileField(upload_to='ipython_notebooks')


class ReportManager(models.Manager):
    def send_reports(self):
        # Get reports that should be sent now, that haven't already been sent this hour
        reports = self.filter(day_of_week=now().day, hour=now().hour)
        reports = reports.exclude(sent_reports__timestamp__hour=now().hour)

        for report in reports:
            report.notebook.evaluate()
            report.send()


class Report(models.Model):
    """
    Someone who's interested in receiving a report on a regular basis
    """
    notebook = models.ForeignKey(Notebook)
    email = models.EmailField(
        help_text="The email address of someone who wants a report sent to them"
    )
    day_of_week = models.PositiveIntegerField(
        help_text="The day of the week when this report should be sent"
    )
    hour = models.PositiveIntegerField(
        help_text="The hour of the day in UTC when this report should be sent"
    )


class SentReport(models.Model):
    report = models.ForeignKey(Report, related_name='sent_reports')
    output = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
