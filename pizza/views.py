from django.http import HttpResponse
from .models import Pizza
import json

def index(request, pid):
    try:
        pizza = Pizza.objects.get(id=pid)

        return HttpResponse(
            content=json.dumps({
                'id': pizza.id,
                'title': pizza.title,
                'description': pizza.description,
            })
        )
    except:
        return HttpResponse(
            content=json.dumps({
                "status": "error",
                "message": "pizza not found"
            })
        )

def random(request):
    pizzas = Pizza.objects.exclude(likes__user=request.user).order_by("?")[:15].values()

    return HttpResponse(list(pizzas))