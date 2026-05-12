from django.test import TestCase
from exams.models import ExamResult


class ExamResultQueryTests(TestCase):
    def setUp(self):
        ExamResult.objects.bulk_create([
            ExamResult(student_name="A", course="Math", score=14),
            ExamResult(student_name="B", course="Math", score=10),
            ExamResult(student_name="C", course="Math", score=5),
        ])

    def test_filter_passed_results_default_threshold(self):
        results = ExamResult.objects.filter(score__gte=10).order_by("-score")

        scores = [r.score for r in results]

        self.assertEqual(scores, [14, 10])

    def test_filter_with_custom_threshold(self):
        results = ExamResult.objects.filter(score__gte=12).order_by("-score")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].student_name, "A")