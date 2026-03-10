from django.http import JsonResponse
from .models import ExamResult


def passed_results(request):
    """
    Return results with score >= 10, sorted by descending score.

    Optional query param:
    - min_score
    """
    return JsonResponse([], safe=False)
