from django.db import models


class NotebookReport(models.Model):
    notebook = models.FileField(upload_to='ipython_notebooks')


class NotebookReportee(models.Model):
    """
    Someone who's interested in receiving a report on a regular basis
    """
    report = models.ForeignKey(NotebookReport)
    email = models.EmailField(
        help_text="The email address of someone who wants a report sent to them"
    )


class NoteBookReportTimes(models.Model):
    """
    A time when a report for this notebook should be generated and sent
    """
    report = models.ForeignKey(NotebookReport)
    send_time = models.DateTimeField(
        help_text="A time when the report should be sent, respsects the project timezone setting"
    )
