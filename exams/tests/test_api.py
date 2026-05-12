from django.test import TestCase
from django.urls import reverse
from exams.models import ExamResult

pytest_plugins = "django"

class PassedResultsAPITests(TestCase):
    def setUp(self):
        ExamResult.objects.create(student_name="Alice", course="Math", score=14.5)
        ExamResult.objects.create(student_name="Bob", course="Math", score=10.0)
        ExamResult.objects.create(student_name="Charlie", course="Math", score=8.0)

    def test_default_min_score(self):
        response = self.client.get(reverse("passed_results"))

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["student_name"], "Alice")

    def test_min_score_filter(self):
        response = self.client.get(reverse("passed_results"), {"min_score": 12})

        data = response.json()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["student_name"], "Alice")

    def test_invalid_min_score(self):
        response = self.client.get(reverse("passed_results"), {"min_score": "abc"})

        self.assertEqual(response.status_code, 400)