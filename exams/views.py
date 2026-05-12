import logging

from django.http import JsonResponse
from .models import ExamResult

logger = logging.getLogger(__name__)


def passed_results(request):
    """
    Return results with score >= 10, sorted by descending score.

    Optional query param:
    - min_score
    """
    min_score_param = request.GET.get("min_score", "10")
    logger.critical(f"min_score_param: {min_score_param}")

    try:
        min_score = float(min_score_param)
    except ValueError:
        return JsonResponse(
            {"error": "min_score must be a valid number."},
            status=400,
        )

    results = (
        ExamResult.objects
            .filter(score__gte=min_score)
            .order_by("-score")
            .values("student_name", "course", "score")
    )

    return JsonResponse(list(results), safe=False)