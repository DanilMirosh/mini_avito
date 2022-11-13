import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from ads.models import Ad


@method_decorator(csrf_exempt, name='dispatch')
class AdListView(View):
    """Get all ads"""

    def get(self, request):
        ads = Ad.objects.all()
        response = []
        for ad in ads:
            response.append(
                {
                    'id': ad.id,
                    'name': ad.name,
                    'author': ad.author,
                    'price': ad.price,
                    'description': ad.description,
                    'address': ad.address,
                    'is_published': ad.is_published
                }
            )

        return JsonResponse(response, safe=False, status=200)

    """Get a new ad"""

    def post(self, request):
        data = json.loads(request.body)
        ad = Ad(**data)
        ad.save()

        return JsonResponse(
            {
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            }, status=201
        )


class AdDetailView(DetailView):
    model = Ad

    """Get ad by pk"""

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse(
            {
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            }
        )
