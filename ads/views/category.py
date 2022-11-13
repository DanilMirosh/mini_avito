import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    """Get all categories"""

    def get(self, request):
        categories = Category.objects.all()
        response = []
        for cat in categories:
            response.append(
                {
                    'id': cat.pk,
                    'name': cat.name,
                }
            )

        return JsonResponse(response, safe=False, status=200)

    """Get a new ad"""

    def post(self, request):
        data = json.loads(request.body)
        cat = Category(**data)
        cat.save()

        return JsonResponse(
            {
                'id': cat.id,
                'name': cat.name,
            }, status=201
        )


class CategoryView(DetailView):
    model = Category

    """Get category by pk"""

    def get(self, request, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse(
            {
                'id': cat.id,
                'name': cat.name,
            }
        )
