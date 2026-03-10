from django.db import models


class ExamResult(models.Model):
    student_name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    score = models.FloatField()

    def __str__(self):
        return f"{self.student_name} - {self.course} ({self.score})"
