from django.test import TestCase
from exams.models import ExamResult


class ExamResultModelTests(TestCase):
    def test_str_representation(self):
        result = ExamResult.objects.create(
            student_name="Alice",
            course="Math",
            score=14.5,
        )

        self.assertEqual(str(result), "Alice - Math (14.5)")