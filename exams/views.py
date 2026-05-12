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

    # retrieve the min_score parameter from the request, if it doesn't exist, use 10 by default.
    min_score_param = request.GET.get("min_score", "10")
    logger.info(f"min_score_param: {min_score_param}")

    # Validation logic - `min_score` must be a valid number
    try:
        min_score = float(min_score_param)
    except ValueError:
        return JsonResponse(
            {"error": "min_score must be a valid number."},
            status=400,
        )

    # Validation logic - `min_score` must be between 0 and 20
    if not (0 <= min_score <= 20):
        return JsonResponse(
            {"error": "min_score must be between 0 and 20."},
            status=400,
        )

    # Filter the ExamResult objects based on the min_score parameter and keep only the fields we need.
    # Using Django REST Framework could be considered for larger APIs, as it provides serializers
    # that separate serialization logic from the view layer.
    results = (
        ExamResult.objects
        .filter(score__gte=min_score)
        .order_by("-score")
        .values("student_name", "course", "score")
    )

    # Django's JsonResponse expects a dictionary by default. To return a raw list, we must set safe=False, which
    # disables the dict-only constraint. This is safe in our current case, as the data is not user-generated.
    #
    # In larger or more complex APIs, a structured serialization layer (such as Django REST Framework and Ninja)
    # may be preferable, as it provides consistent output formatting, validation, and easier extensibility
    return JsonResponse(list(results), safe=False)